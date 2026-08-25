namespace ScanPlantAPI.Services.ExternalProviders;

internal interface IPlantIdentificationProvider
{
    Task<PlantIdentificationResult> IdentifyAsync(PlantIdentificationRequest request, CancellationToken cancellationToken);
}

internal interface IPlantKnowledgeProvider
{
    Task<PlantKnowledgeResult?> GetKnowledgeAsync(PlantKnowledgeRequest request, CancellationToken cancellationToken);
}

internal sealed record PlantIdentificationRequest(ValidatedImage Image);

internal sealed record PlantIdentificationResult(IReadOnlyList<PlantIdentificationCandidate> Candidates)
{
    public static PlantIdentificationResult NoMatch { get; } = new([]);
}

internal sealed record PlantIdentificationCandidate(string ScientificName, string? CommonName, decimal Score);

internal sealed record PlantKnowledgeRequest(string ScientificName);

internal sealed record PlantKnowledgeResult(string? CareInstructions, string? Description, string? SafetyNotes);

internal sealed record ExternalFallbackResult(PlantIdentificationResult Identification, PlantKnowledgeResult? Knowledge);
