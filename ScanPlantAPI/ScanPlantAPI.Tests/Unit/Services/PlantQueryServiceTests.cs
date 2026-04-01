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

    [Fact]
    public async Task GetCommunityPlantsAsync_AppliesCityFamilyAndReminderFilters()
    {
        await using var context = CreateContext();
        var expectedPlant = CreatePlant(
            "filtered-plant",
            isInCommunity: true,
            createdAt: new DateTime(2026, 3, 30, 10, 0, 0, DateTimeKind.Utc),
            city: "Sao Paulo",
            family: "Araceae",
            reminderEnabled: true);

        context.Plants.AddRange(
            expectedPlant,
            CreatePlant(
                "wrong-city",
                isInCommunity: true,
                createdAt: new DateTime(2026, 3, 29, 10, 0, 0, DateTimeKind.Utc),
                city: "Curitiba",
                family: "Araceae",
                reminderEnabled: true),
            CreatePlant(
                "wrong-family",
                isInCommunity: true,
                createdAt: new DateTime(2026, 3, 28, 10, 0, 0, DateTimeKind.Utc),
                city: "Sao Paulo",
                family: "Orchidaceae",
                reminderEnabled: true),
            CreatePlant(
                "wrong-reminder",
                isInCommunity: true,
                createdAt: new DateTime(2026, 3, 27, 10, 0, 0, DateTimeKind.Utc),
                city: "Sao Paulo",
                family: "Araceae",
                reminderEnabled: false),
            CreatePlant(
                "private-plant",
                isInCommunity: false,
                createdAt: new DateTime(2026, 3, 26, 10, 0, 0, DateTimeKind.Utc),
                city: "Sao Paulo",
                family: "Araceae",
                reminderEnabled: true));

        await context.SaveChangesAsync();

        var service = new PlantQueryService(context);

        var result = await service.GetCommunityPlantsAsync(new PlantQueryFilters("sao", "ara", true));

        result.Should().ContainSingle();
        result.Single().ScientificName.Should().Be(expectedPlant.ScientificName);
    }

    [Fact]
    public async Task GetUserPlantsAsync_ReturnsOnlyPlantsFromTheRequestedUser_OrderedByCreatedAtDescending()
    {
        await using var context = CreateContext();
        var newestPlant = CreatePlant(
            "newest-user-plant",
            isInCommunity: true,
            createdAt: new DateTime(2026, 3, 30, 10, 0, 0, DateTimeKind.Utc),
            userId: "user-1");
        var oldestPlant = CreatePlant(
            "oldest-user-plant",
            isInCommunity: true,
            createdAt: new DateTime(2026, 3, 28, 10, 0, 0, DateTimeKind.Utc),
            userId: "user-1");

        context.Plants.AddRange(
            newestPlant,
            oldestPlant,
            CreatePlant(
                "other-user-plant",
                isInCommunity: true,
                createdAt: new DateTime(2026, 3, 29, 10, 0, 0, DateTimeKind.Utc),
                userId: "user-2"));

        await context.SaveChangesAsync();

        var service = new PlantQueryService(context);

        var result = await service.GetUserPlantsAsync("user-1");

        result.Should().HaveCount(2);
        result.Select(plant => plant.ScientificName).Should().ContainInOrder(
            newestPlant.ScientificName,
            oldestPlant.ScientificName);
        result.Should().OnlyContain(plant => plant.UserId == "user-1");
    }

    [Fact]
    public async Task GetOrphanedPlantsAsync_ReturnsOnlyPlantsWithoutAnOwner_OrderedByCreatedAtDescending()
    {
        await using var context = CreateContext();
        var newestOrphan = CreatePlant(
            "newest-orphan",
            isInCommunity: true,
            createdAt: new DateTime(2026, 3, 30, 10, 0, 0, DateTimeKind.Utc));
        var oldestOrphan = CreatePlant(
            "oldest-orphan",
            isInCommunity: true,
            createdAt: new DateTime(2026, 3, 28, 10, 0, 0, DateTimeKind.Utc));

        context.Plants.AddRange(
            newestOrphan,
            oldestOrphan,
            CreatePlant(
                "owned-plant",
                isInCommunity: true,
                createdAt: new DateTime(2026, 3, 29, 10, 0, 0, DateTimeKind.Utc),
                userId: "user-1"));

        await context.SaveChangesAsync();

        var service = new PlantQueryService(context);

        var result = await service.GetOrphanedPlantsAsync();

        result.Should().HaveCount(2);
        result.Select(plant => plant.ScientificName).Should().ContainInOrder(
            newestOrphan.ScientificName,
            oldestOrphan.ScientificName);
        result.Should().OnlyContain(plant => plant.UserId == null);
    }

    private static ApplicationDbContext CreateContext()
    {
        var options = new DbContextOptionsBuilder<ApplicationDbContext>()
            .UseInMemoryDatabase(Guid.NewGuid().ToString())
            .Options;

        return new ApplicationDbContext(options);
    }

    private static Plant CreatePlant(
        string scientificName,
        bool isInCommunity,
        DateTime createdAt,
        string? city = null,
        string? family = null,
        bool reminderEnabled = false,
        string? userId = null)
    {
        return new Plant
        {
            UserId = userId,
            ScientificName = scientificName,
            CommonName = scientificName,
            City = city,
            Family = family,
            IsInCommunity = isInCommunity,
            ReminderEnabled = reminderEnabled,
            CreatedAt = createdAt,
            UpdatedAt = createdAt
        };
    }
}
