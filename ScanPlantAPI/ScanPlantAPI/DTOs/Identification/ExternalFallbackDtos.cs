namespace ScanPlantAPI.DTOs.Identification;

public sealed class ExternalFallbackResponseDto
{
    public string Source { get; init; } = "external_fallback";
    public string MatchStatus { get; init; } = "no_match";
    public ExternalPlantIdentificationDto? Identification { get; init; }
    public IReadOnlyList<ExternalPlantCandidateDto> Candidates { get; init; } = [];
    public ExternalPlantKnowledgeDto? Knowledge { get; init; }
    public string KnowledgeStatus { get; init; } = "not_requested";
}

public sealed class ExternalPlantIdentificationDto
{
    public string ScientificName { get; init; } = string.Empty;
    public string? CommonName { get; init; }
}

public sealed class ExternalPlantCandidateDto
{
    public string ScientificName { get; init; } = string.Empty;
    public string? CommonName { get; init; }
    public decimal Score { get; init; }
}

public sealed class ExternalPlantKnowledgeDto
{
    public string? CareInstructions { get; init; }
    public string? Description { get; init; }
    public string? SafetyNotes { get; init; }
}
