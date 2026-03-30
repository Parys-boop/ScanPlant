using FluentAssertions;
using Microsoft.EntityFrameworkCore;
using ScanPlantAPI.Data;
using ScanPlantAPI.Models;
using ScanPlantAPI.Services.Plants;
using Xunit;

namespace ScanPlantAPI.Tests.Unit.Services;

public class PlantQueryServiceTests
{
    [Fact]
    public async Task GetCommunityPlantsAsync_ReturnsOnlyCommunityPlants_OrderedByCreatedAtDescending()
    {
        await using var context = CreateContext();
        var oldestCommunityPlant = CreatePlant("oldest-community", isInCommunity: true, createdAt: new DateTime(2026, 3, 27, 10, 0, 0, DateTimeKind.Utc));
        var privatePlant = CreatePlant("private-plant", isInCommunity: false, createdAt: new DateTime(2026, 3, 29, 10, 0, 0, DateTimeKind.Utc));
        var newestCommunityPlant = CreatePlant("newest-community", isInCommunity: true, createdAt: new DateTime(2026, 3, 30, 10, 0, 0, DateTimeKind.Utc));

        context.Plants.AddRange(oldestCommunityPlant, privatePlant, newestCommunityPlant);
        await context.SaveChangesAsync();

        var service = new PlantQueryService(context);

        var result = await service.GetCommunityPlantsAsync(new PlantQueryFilters());

        result.Should().HaveCount(2);
        result.Select(plant => plant.ScientificName).Should().ContainInOrder(
            newestCommunityPlant.ScientificName,
            oldestCommunityPlant.ScientificName);
        result.Should().OnlyContain(plant => plant.IsInCommunity);
    }

    private static ApplicationDbContext CreateContext()
    {
        var options = new DbContextOptionsBuilder<ApplicationDbContext>()
            .UseInMemoryDatabase(Guid.NewGuid().ToString())
            .Options;

        return new ApplicationDbContext(options);
    }

    private static Plant CreatePlant(string scientificName, bool isInCommunity, DateTime createdAt)
    {
        return new Plant
        {
            ScientificName = scientificName,
            CommonName = scientificName,
            IsInCommunity = isInCommunity,
            CreatedAt = createdAt,
            UpdatedAt = createdAt
        };
    }
}
