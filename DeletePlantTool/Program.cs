using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

// Script principal
var optionsBuilder = new DbContextOptionsBuilder<ApplicationDbContext>();
var connectionString = Environment.GetEnvironmentVariable("DATABASE_URL")
    ?? throw new InvalidOperationException("DATABASE_URL não configurada.");
optionsBuilder.UseNpgsql(connectionString);

using var context = new ApplicationDbContext(optionsBuilder.Options);

Console.WriteLine("Procurando plantas com 'Chlorophytum comosum', 'Spingo' ou 'Espinho de Passarinho'...\n");

var plants = await context.Plants
    .Where(p => 
        (p.ScientificName != null && p.ScientificName.Contains("Chlorophytum comosum")) ||
        (p.CommonName != null && (p.CommonName.Contains("Spingo") || p.CommonName.Contains("Espinho de Passarinho")))
    )
    .ToListAsync();

if (!plants.Any())
{
    Console.WriteLine("❌ Nenhuma planta encontrada com esses critérios.");
    return;
}

Console.WriteLine($"✅ Encontradas {plants.Count} planta(s):\n");
foreach (var plant in plants)
{
    Console.WriteLine($"  📌 ID: {plant.Id}");
    Console.WriteLine($"  🔬 Nome Científico: {plant.ScientificName}");
    Console.WriteLine($"  🌿 Nome Comum: {plant.CommonName}");
    Console.WriteLine($"  🏷️  Família: {plant.Family}");
    Console.WriteLine($"  👤 User ID: {plant.UserId ?? "N/A"}");
    Console.WriteLine("  " + new string('-', 50));
}

Console.Write("\n⚠️  Deseja EXCLUIR todas essas plantas do banco de dados? (S/N): ");
var confirm = Console.ReadLine();

if (confirm?.ToUpper() == "S" || confirm?.ToUpper() == "SIM")
{
    context.Plants.RemoveRange(plants);
    int deleted = await context.SaveChangesAsync();
    Console.WriteLine($"\n✅ {deleted} planta(s) excluída(s) com sucesso!");
}
else
{
    Console.WriteLine("\n❌ Operação cancelada. Nenhuma planta foi excluída.");
}

// Modelos
public class ApplicationUser : IdentityUser
{
    public string? Name { get; set; }
    public string? Phone { get; set; }
    public string? Bio { get; set; }
    public string? AvatarUrl { get; set; }
    public string? ExperienceLevel { get; set; }
    public string? PlantPreference { get; set; }
    public string? City { get; set; }
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
}

public class Plant
{
    [Key]
    public Guid Id { get; set; } = Guid.NewGuid();
    public string? UserId { get; set; }
    [Required]
    [MaxLength(500)]
    public string ScientificName { get; set; } = string.Empty;
    [MaxLength(500)]
    public string? CommonName { get; set; }
    [MaxLength(500)]
    public string? Family { get; set; }
    [MaxLength(500)]
    public string? Genus { get; set; }
    public string? WikiDescription { get; set; }
    public string? CareInstructions { get; set; }
    public string? ImageData { get; set; }
    public string? ImageUrl { get; set; }
    [Column(TypeName = "decimal(10, 7)")]
    public decimal? Latitude { get; set; }
    [Column(TypeName = "decimal(10, 7)")]
    public decimal? Longitude { get; set; }
    [MaxLength(200)]
    public string? City { get; set; }
    [MaxLength(500)]
    public string? LocationName { get; set; }
    public int? WateringFrequencyDays { get; set; }
    public string? WateringFrequencyText { get; set; }
    public bool ReminderEnabled { get; set; } = false;
    public string? ReminderNotificationId { get; set; }
    public string? Notes { get; set; }
    public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
}

public class ApplicationDbContext : IdentityDbContext<ApplicationUser>
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }
    public DbSet<Plant> Plants { get; set; }
}
