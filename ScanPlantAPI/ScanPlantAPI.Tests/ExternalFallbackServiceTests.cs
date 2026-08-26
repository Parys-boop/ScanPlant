using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging.Abstractions;
using Microsoft.Extensions.Options;
using ScanPlantAPI.Services.ExternalProviders;

namespace ScanPlantAPI.Tests;

public sealed class ExternalFallbackServiceTests
{
    [Fact]
    public async Task ExecuteAsync_WithoutConsent_DoesNotCallTheIdentificationProvider()
    {
        var identification = new FakeIdentificationProvider();
        var service = CreateService(identification, new FakeKnowledgeProvider());

        var result = await service.ExecuteAsync(ValidUpload(consentToExternalProcessing: false), CancellationToken.None);

        Assert.Equal(ExternalFallbackUploadFailure.ConsentRequired, result.UploadFailure);
        Assert.Equal(0, identification.Calls);
    }

    [Fact]
    public async Task ExecuteAsync_WhenIdentificationTimesOut_ReturnsTimedOutWithoutRetry()
    {
        var identification = new FakeIdentificationProvider(async (_, cancellationToken) =>
        {
            await Task.Delay(Timeout.InfiniteTimeSpan, cancellationToken);
            return PlantIdentificationResult.NoMatch;
        });
        var service = CreateService(identification, new FakeKnowledgeProvider(), requestTimeoutSeconds: 1);

        var result = await service.ExecuteAsync(ValidUpload(), CancellationToken.None);

        Assert.True(result.TimedOut);
        Assert.Equal(1, identification.Calls);
    }

    [Fact]
    public async Task ExecuteAsync_WhenGroqThrowsUnexpectedFailure_KeepsIdentificationSafe()
    {
        var knowledge = new FakeKnowledgeProvider((_, _) => throw new InvalidOperationException("synthetic-sensitive-value"));
        var service = CreateService(new FakeIdentificationProvider(), knowledge, groqEnabled: true);

        var result = await service.ExecuteAsync(ValidUpload(), CancellationToken.None);

        Assert.NotNull(result.Result);
        Assert.Equal("failed", result.KnowledgeStatus);
        Assert.Null(result.Result!.Knowledge);
    }

    private static ExternalFallbackService CreateService(
        FakeIdentificationProvider identification,
        FakeKnowledgeProvider knowledge,
        int requestTimeoutSeconds = 20,
        bool groqEnabled = false)
    {
        var options = Options.Create(new ExternalFallbackOptions
        {
            MaxImageBytes = 20 * 1024,
            MaxImageWidth = 4096,
            MaxImageHeight = 4096,
            RequestTimeoutSeconds = requestTimeoutSeconds,
            AllowedMediaTypes = ["image/jpeg", "image/png"]
        });
        var configuration = new ConfigurationBuilder().AddInMemoryCollection(new Dictionary<string, string?>
        {
            ["Groq:Enabled"] = groqEnabled.ToString()
        }).Build();
        return new ExternalFallbackService(new ExternalFallbackUploadValidator(options), identification, knowledge, options, configuration, NullLogger<ExternalFallbackService>.Instance);
    }

    private static ExternalFallbackUpload ValidUpload(bool consentToExternalProcessing = true)
    {
        var image = new MemoryStream(File.ReadAllBytes(Path.Combine(AppContext.BaseDirectory, "Fixtures", "daisy.jpg")));
        return new ExternalFallbackUpload(image, image.Length, "image/jpeg", consentToExternalProcessing);
    }

    private sealed class FakeIdentificationProvider : IPlantIdentificationProvider
    {
        private readonly Func<PlantIdentificationRequest, CancellationToken, Task<PlantIdentificationResult>> _identify;
        public int Calls { get; private set; }
        public FakeIdentificationProvider(Func<PlantIdentificationRequest, CancellationToken, Task<PlantIdentificationResult>>? identify = null) => _identify = identify ?? ((_, _) => Task.FromResult(new PlantIdentificationResult([new PlantIdentificationCandidate("Ficus lyrata", null, 0.98m)])));
        public Task<PlantIdentificationResult> IdentifyAsync(PlantIdentificationRequest request, CancellationToken cancellationToken)
        {
            Calls++;
            return _identify(request, cancellationToken);
        }
    }

    private sealed class FakeKnowledgeProvider : IPlantKnowledgeProvider
    {
        private readonly Func<PlantKnowledgeRequest, CancellationToken, Task<PlantKnowledgeResult?>> _knowledge;
        public FakeKnowledgeProvider(Func<PlantKnowledgeRequest, CancellationToken, Task<PlantKnowledgeResult?>>? knowledge = null) => _knowledge = knowledge ?? ((_, _) => Task.FromResult<PlantKnowledgeResult?>(null));
        public Task<PlantKnowledgeResult?> GetKnowledgeAsync(PlantKnowledgeRequest request, CancellationToken cancellationToken) => _knowledge(request, cancellationToken);
    }
}
