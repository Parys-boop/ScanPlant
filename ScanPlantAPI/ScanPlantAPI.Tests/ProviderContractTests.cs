using ScanPlantAPI.DTOs.Identification;
using ScanPlantAPI.Services.ExternalProviders;

namespace ScanPlantAPI.Tests;

public sealed class ExternalFallbackProviderContractTests
{
    [Fact]
    public async Task IdentificationProviderFake_UsesNeutralRequestAndResult()
    {
        IPlantIdentificationProvider provider = new FakeIdentificationProvider();
        var image = new ValidatedImage([1, 2], "image/png", 1, 1);

        var result = await provider.IdentifyAsync(new PlantIdentificationRequest(image), CancellationToken.None);

        Assert.Equal("Ficus lyrata", Assert.Single(result.Candidates).ScientificName);
    }

    [Fact]
    public async Task KnowledgeProviderFake_ReceivesOnlyNormalizedScientificName()
    {
        IPlantKnowledgeProvider provider = new FakeKnowledgeProvider();

        var result = await provider.GetKnowledgeAsync(new PlantKnowledgeRequest("Ficus lyrata"), CancellationToken.None);

        var knowledge = Assert.IsType<PlantKnowledgeResult>(result);
        Assert.Equal("Indirect light", knowledge.CareInstructions);
    }

    [Fact]
    public void PublicResponseDto_DoesNotExposeProviderFields()
    {
        var propertyNames = typeof(ExternalFallbackResponseDto).GetProperties().Select(property => property.Name);

        Assert.DoesNotContain(propertyNames, name => name.Contains("Provider", StringComparison.OrdinalIgnoreCase));
        Assert.DoesNotContain(propertyNames, name => name.Contains("ApiKey", StringComparison.OrdinalIgnoreCase));
        Assert.DoesNotContain(propertyNames, name => name.Contains("Url", StringComparison.OrdinalIgnoreCase));
        Assert.DoesNotContain(propertyNames, name => name.Contains("Payload", StringComparison.OrdinalIgnoreCase));
    }

    private sealed class FakeIdentificationProvider : IPlantIdentificationProvider
    {
        public Task<PlantIdentificationResult> IdentifyAsync(PlantIdentificationRequest request, CancellationToken cancellationToken)
        {
            return Task.FromResult(new PlantIdentificationResult([
                new PlantIdentificationCandidate("Ficus lyrata", "Fiddle-leaf fig", 0.98m)
            ]));
        }
    }

    private sealed class FakeKnowledgeProvider : IPlantKnowledgeProvider
    {
        public Task<PlantKnowledgeResult?> GetKnowledgeAsync(PlantKnowledgeRequest request, CancellationToken cancellationToken)
        {
            return Task.FromResult<PlantKnowledgeResult?>(new PlantKnowledgeResult("Indirect light", null, null));
        }
    }
}
