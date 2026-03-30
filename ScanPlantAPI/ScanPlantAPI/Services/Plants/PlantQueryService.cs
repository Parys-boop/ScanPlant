using Microsoft.EntityFrameworkCore;
using ScanPlantAPI.Data;
using ScanPlantAPI.Models;

namespace ScanPlantAPI.Services.Plants;

public sealed record PlantQueryFilters(string? City = null, string? Family = null, bool? ReminderEnabled = null);

public interface IPlantQueryService
{
    Task<List<Plant>> GetCommunityPlantsAsync(PlantQueryFilters filters, CancellationToken cancellationToken = default);
    Task<List<Plant>> GetUserPlantsAsync(string? userId, CancellationToken cancellationToken = default);
    Task<List<Plant>> GetOrphanedPlantsAsync(CancellationToken cancellationToken = default);
}

public sealed class PlantQueryService : IPlantQueryService
{
    private readonly ApplicationDbContext _context;

    public PlantQueryService(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<List<Plant>> GetCommunityPlantsAsync(PlantQueryFilters filters, CancellationToken cancellationToken = default)
    {
        var query = _context.Plants
            .AsNoTracking()
            .Where(p => p.IsInCommunity);

        if (!string.IsNullOrWhiteSpace(filters.City))
        {
            var normalizedCity = filters.City.Trim().ToLower();
            query = query.Where(p => p.City != null && p.City.ToLower().Contains(normalizedCity));
        }

        if (!string.IsNullOrWhiteSpace(filters.Family))
        {
            var normalizedFamily = filters.Family.Trim().ToLower();
            query = query.Where(p => p.Family != null && p.Family.ToLower().Contains(normalizedFamily));
        }

        if (filters.ReminderEnabled.HasValue)
        {
            query = query.Where(p => p.ReminderEnabled == filters.ReminderEnabled.Value);
        }

        return await query
            .OrderByDescending(p => p.CreatedAt)
            .ToListAsync(cancellationToken);
    }

    public async Task<List<Plant>> GetUserPlantsAsync(string? userId, CancellationToken cancellationToken = default)
    {
        return await _context.Plants
            .AsNoTracking()
            .Where(p => p.UserId == userId)
            .OrderByDescending(p => p.CreatedAt)
            .ToListAsync(cancellationToken);
    }

    public async Task<List<Plant>> GetOrphanedPlantsAsync(CancellationToken cancellationToken = default)
    {
        return await _context.Plants
            .AsNoTracking()
            .Where(p => p.UserId == null)
            .OrderByDescending(p => p.CreatedAt)
            .ToListAsync(cancellationToken);
    }
}
