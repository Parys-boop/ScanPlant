using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Storage;
using Npgsql;
using ScanPlantAPI.Data;

namespace ScanPlantAPI.Services;

public sealed class Phase0DatabaseException : Exception
{
    public Phase0DatabaseException(string message) : base(message)
    {
    }
}

public static class Phase0DatabaseInitializer
{
    private const string DatabaseName = "ScanPlantPhase0";

    public static void ValidateConnectionTarget(string connectionString)
    {
        var builder = new NpgsqlConnectionStringBuilder(connectionString);
        if (!string.Equals(builder.Database, DatabaseName, StringComparison.OrdinalIgnoreCase))
        {
            throw new Phase0DatabaseException($"O modo Fase 0 aceita somente o banco {DatabaseName}.");
        }
    }

    public static async Task EnsureReadyAsync(IServiceProvider services, CancellationToken cancellationToken)
    {
        using var scope = services.CreateScope();
        var dbContext = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();
        var logger = scope.ServiceProvider.GetRequiredService<ILogger<ApplicationDbContext>>();
        var creator = dbContext.Database.GetService<IRelationalDatabaseCreator>();

        bool exists;
        try
        {
            exists = await creator.ExistsAsync(cancellationToken);
        }
        catch
        {
            throw new Phase0DatabaseException("Não foi possível verificar o banco isolado da Fase 0.");
        }

        if (!exists)
        {
            logger.LogInformation("Criando e migrando o banco isolado da Fase 0.");
            try
            {
                await dbContext.Database.MigrateAsync(cancellationToken);
                return;
            }
            catch
            {
                throw new Phase0DatabaseException("Não foi possível criar o banco isolado da Fase 0.");
            }
        }

        try
        {
            var pendingMigrations = await dbContext.Database.GetPendingMigrationsAsync(cancellationToken);
            if (pendingMigrations.Any())
            {
                throw new Phase0DatabaseException("O banco isolado existente está incompatível: há migrations pendentes. Ele não foi alterado.");
            }

            await ValidateMappedColumnsAsync(dbContext, cancellationToken);
        }
        catch (Phase0DatabaseException)
        {
            throw;
        }
        catch
        {
            throw new Phase0DatabaseException("O banco isolado existente está incompatível ou não possui histórico de migrations. Ele não foi alterado.");
        }
    }

    private static async Task ValidateMappedColumnsAsync(ApplicationDbContext dbContext, CancellationToken cancellationToken)
    {
        var expectedColumns = dbContext.Model.GetEntityTypes()
            .Where(entity => entity.GetTableName() is not null)
            .SelectMany(entity =>
            {
                var tableName = entity.GetTableName()!;
                var schema = entity.GetSchema() ?? "public";
                var storeObject = StoreObjectIdentifier.Table(tableName, schema);
                return entity.GetProperties()
                    .Select(property => (Table: tableName, Column: property.GetColumnName(storeObject)))
                    .Where(column => column.Column is not null);
            })
            .Select(column => $"{column.Table}.{column.Column}")
            .ToHashSet(StringComparer.Ordinal);

        var actualColumns = new HashSet<string>(StringComparer.Ordinal);
        var connection = dbContext.Database.GetDbConnection();
        await connection.OpenAsync(cancellationToken);
        try
        {
            await using var command = connection.CreateCommand();
            command.CommandText = "SELECT table_name, column_name FROM information_schema.columns WHERE table_schema = 'public';";
            await using var reader = await command.ExecuteReaderAsync(cancellationToken);
            while (await reader.ReadAsync(cancellationToken))
            {
                actualColumns.Add($"{reader.GetString(0)}.{reader.GetString(1)}");
            }
        }
        finally
        {
            await connection.CloseAsync();
        }

        if (expectedColumns.Any(column => !actualColumns.Contains(column)))
        {
            throw new Phase0DatabaseException("O banco isolado existente está incompatível com o modelo atual. Ele não foi alterado.");
        }
    }
}
