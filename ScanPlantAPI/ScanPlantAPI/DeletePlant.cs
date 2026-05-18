using Microsoft.EntityFrameworkCore;
using ScanPlantAPI.Data;
using ScanPlantAPI.Models;

namespace ScanPlantAPI;

public class DeletePlantScript
{
    public static async Task Main(string[] args)
    {
        var optionsBuilder = new DbContextOptionsBuilder<ApplicationDbContext>();
        var connectionString = Environment.GetEnvironmentVariable("DATABASE_URL")
            ?? throw new InvalidOperationException("DATABASE_URL não configurada.");
        optionsBuilder.UseNpgsql(connectionString);

        using var context = new ApplicationDbContext(optionsBuilder.Options);

        // Buscar plantas com o nome científico ou comum contendo as palavras-chave
        var plants = await context.Plants
            .Where(p => 
                (p.ScientificName != null && p.ScientificName.Contains("Chlorophytum comosum")) ||
                (p.CommonName != null && (p.CommonName.Contains("Spingo") || p.CommonName.Contains("Espinho de Passarinho")))
            )
            .ToListAsync();

        if (!plants.Any())
        {
            Console.WriteLine("Nenhuma planta encontrada com esses critérios.");
            return;
        }

        Console.WriteLine($"Encontradas {plants.Count} planta(s):");
        foreach (var plant in plants)
        {
            Console.WriteLine($"  ID: {plant.Id}");
            Console.WriteLine($"  Nome Científico: {plant.ScientificName}");
            Console.WriteLine($"  Nome Comum: {plant.CommonName}");
            Console.WriteLine($"  Família: {plant.Family}");
            Console.WriteLine("  ---");
        }

        Console.WriteLine("\nDeseja excluir todas essas plantas? (S/N)");
        var confirm = Console.ReadLine();

        if (confirm?.ToUpper() == "S")
        {
            context.Plants.RemoveRange(plants);
            await context.SaveChangesAsync();
            Console.WriteLine($"\n{plants.Count} planta(s) excluída(s) com sucesso!");
        }
        else
        {
            Console.WriteLine("\nOperação cancelada.");
        }
    }
}
