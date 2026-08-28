using System.Buffers.Binary;
using System.IO.Compression;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging.Abstractions;
using Microsoft.Extensions.Options;
using ScanPlantAPI.Services.ExternalProviders;
using Xunit;

namespace ScanPlantAPI.MutationHarness;

public sealed class ExternalFallbackMutationHarnessTests
{
    [Fact]
    public async Task ValidateAsync_WhenUploadIsMissing_RejectsIt()
    {
        var result = await CreateValidator().ValidateAsync(new ExternalFallbackUpload(null, null, null, true));

        Assert.Equal(ExternalFallbackUploadFailure.MissingImage, result.Failure);
        Assert.False(result.IsValid);
    }

    [Fact]
    public async Task ValidateAsync_WhenConsentIsMissing_RejectsBeforeReadingImage()
    {
        await using var image = Png(1, 1);

        var result = await CreateValidator().ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/png", false));

        Assert.Equal(ExternalFallbackUploadFailure.ConsentRequired, result.Failure);
        Assert.False(result.IsValid);
    }

    [Fact]
    public async Task ValidateAsync_WhenMimeDoesNotMatchDecodedImage_RejectsIt()
    {
        await using var image = Png(1, 1);

        var result = await CreateValidator().ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/jpeg", true));

        Assert.Equal(ExternalFallbackUploadFailure.InvalidImageSignature, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenDimensionsExceedLimit_RejectsIt()
    {
        await using var image = Png(2, 1);

        var result = await CreateValidator(maxImageDimension: 1).ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/png", true));

        Assert.Equal(ExternalFallbackUploadFailure.InvalidImageDimensions, result.Failure);
    }

    [Fact]
    public async Task ExecuteAsync_WhenConsentIsMissing_DoesNotCallProvider()
    {
        var identification = new FakeIdentificationProvider();
        var result = await CreateService(identification).ExecuteAsync(ValidUpload(consent: false), CancellationToken.None);

        Assert.Equal(ExternalFallbackUploadFailure.ConsentRequired, result.UploadFailure);
        Assert.Null(result.Result);
        Assert.Equal(0, identification.Calls);
    }

    [Fact]
    public async Task ExecuteAsync_WhenRequestIsCancelled_PropagatesWithoutRetry()
    {
        using var cancelled = new CancellationTokenSource();
        var identification = new FakeIdentificationProvider((_, _) =>
        {
            cancelled.Cancel();
            return Task.FromCanceled<PlantIdentificationResult>(cancelled.Token);
        });

        await Assert.ThrowsAnyAsync<OperationCanceledException>(() => CreateService(identification).ExecuteAsync(ValidUpload(), cancelled.Token));

        Assert.Equal(1, identification.Calls);
    }

    [Fact]
    public async Task ExecuteAsync_WhenIdentificationTimesOut_ReturnsNeutralTimeoutWithoutRetry()
    {
        var identification = new FakeIdentificationProvider(async (_, token) =>
        {
            await Task.Delay(Timeout.InfiniteTimeSpan, token);
            return PlantIdentificationResult.NoMatch;
        });

        var result = await CreateService(identification, requestTimeoutSeconds: 1).ExecuteAsync(ValidUpload(), CancellationToken.None);

        Assert.True(result.TimedOut);
        Assert.Null(result.Result);
        Assert.Equal("not_requested", result.KnowledgeStatus);
        Assert.Equal(1, identification.Calls);
    }

    [Fact]
    public async Task ExecuteAsync_WhenProviderRateLimits_TranslatesFailureWithoutRetry()
    {
        var identification = new FakeIdentificationProvider((_, _) => throw new ExternalProviderRateLimitException("fake", TimeSpan.FromSeconds(2)));

        var result = await CreateService(identification).ExecuteAsync(ValidUpload(), CancellationToken.None);

        Assert.NotNull(result.RateLimitException);
        Assert.Null(result.Result);
        Assert.Equal(1, identification.Calls);
    }

    [Fact]
    public async Task ExecuteAsync_WhenKnowledgeFails_KeepsIdentificationAndDegradesPredictably()
    {
        var knowledge = new FakeKnowledgeProvider((_, _) => throw new InvalidOperationException("synthetic"));

        var result = await CreateService(new FakeIdentificationProvider(), knowledge, groqEnabled: true).ExecuteAsync(ValidUpload(), CancellationToken.None);

        Assert.NotNull(result.Result);
        Assert.Null(result.Result!.Knowledge);
        Assert.Equal("failed", result.KnowledgeStatus);
    }

    [Fact]
    public async Task ExecuteAsync_WhenKnowledgeIsDisabled_ReturnsNeutralIdentificationOnly()
    {
        var knowledge = new FakeKnowledgeProvider();

        var result = await CreateService(new FakeIdentificationProvider(), knowledge, groqEnabled: false).ExecuteAsync(ValidUpload(), CancellationToken.None);

        Assert.NotNull(result.Result);
        Assert.Null(result.Result!.Knowledge);
        Assert.Equal("not_requested", result.KnowledgeStatus);
        Assert.Equal(0, knowledge.Calls);
    }

    private static ExternalFallbackUploadValidator CreateValidator(int maxImageDimension = 4096) => new(Options.Create(CreateOptions(maxImageDimension)));

    private static ExternalFallbackService CreateService(
        FakeIdentificationProvider identification,
        FakeKnowledgeProvider? knowledge = null,
        int requestTimeoutSeconds = 20,
        bool groqEnabled = false)
    {
        var options = Options.Create(CreateOptions(4096, requestTimeoutSeconds));
        var configuration = new ConfigurationBuilder().AddInMemoryCollection(new Dictionary<string, string?>
        {
            ["Groq:Enabled"] = groqEnabled.ToString()
        }).Build();
        return new ExternalFallbackService(
            new ExternalFallbackUploadValidator(options),
            identification,
            knowledge ?? new FakeKnowledgeProvider(),
            options,
            configuration,
            NullLogger<ExternalFallbackService>.Instance);
    }

    private static ExternalFallbackOptions CreateOptions(int maxImageDimension, int requestTimeoutSeconds = 20) => new()
    {
        MaxImageBytes = 20 * 1024,
        MaxImageWidth = maxImageDimension,
        MaxImageHeight = maxImageDimension,
        RequestTimeoutSeconds = requestTimeoutSeconds,
        AllowedMediaTypes = ["image/png", "image/jpeg"]
    };

    private static ExternalFallbackUpload ValidUpload(bool consent = true)
    {
        var image = Png(1, 1);
        return new ExternalFallbackUpload(image, image.Length, "image/png", consent);
    }

    private static MemoryStream Png(uint width, uint height)
    {
        using var output = new MemoryStream();
        output.Write([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);
        var header = new byte[13];
        BinaryPrimitives.WriteUInt32BigEndian(header, width);
        BinaryPrimitives.WriteUInt32BigEndian(header.AsSpan(4), height);
        header[8] = 8;
        header[9] = 6;
        WriteChunk(output, "IHDR"u8, header);

        var rawPixels = new byte[checked((int)(height * (width * 4 + 1)))];
        using var compressed = new MemoryStream();
        using (var zlib = new ZLibStream(compressed, CompressionLevel.SmallestSize, leaveOpen: true))
        {
            zlib.Write(rawPixels);
        }

        WriteChunk(output, "IDAT"u8, compressed.ToArray());
        WriteChunk(output, "IEND"u8, []);
        return new MemoryStream(output.ToArray());
    }

    private static void WriteChunk(Stream output, ReadOnlySpan<byte> type, ReadOnlySpan<byte> data)
    {
        Span<byte> length = stackalloc byte[4];
        BinaryPrimitives.WriteUInt32BigEndian(length, (uint)data.Length);
        output.Write(length);
        output.Write(type);
        output.Write(data);
        BinaryPrimitives.WriteUInt32BigEndian(length, Crc(type, data));
        output.Write(length);
    }

    private static uint Crc(ReadOnlySpan<byte> type, ReadOnlySpan<byte> data)
    {
        var crc = 0xFFFFFFFFu;
        foreach (var value in type)
        {
            crc ^= value;
            for (var bit = 0; bit < 8; bit++)
            {
                crc = (crc >> 1) ^ ((crc & 1) == 1 ? 0xEDB88320u : 0);
            }
        }

        foreach (var value in data)
        {
            crc ^= value;
            for (var bit = 0; bit < 8; bit++)
            {
                crc = (crc >> 1) ^ ((crc & 1) == 1 ? 0xEDB88320u : 0);
            }
        }

        return ~crc;
    }

    private sealed class FakeIdentificationProvider : IPlantIdentificationProvider
    {
        private readonly Func<PlantIdentificationRequest, CancellationToken, Task<PlantIdentificationResult>> _implementation;

        public FakeIdentificationProvider(Func<PlantIdentificationRequest, CancellationToken, Task<PlantIdentificationResult>>? implementation = null) =>
            _implementation = implementation ?? ((_, _) => Task.FromResult(new PlantIdentificationResult([new PlantIdentificationCandidate("Ficus lyrata", null, 0.98m)])));

        public int Calls { get; private set; }

        public Task<PlantIdentificationResult> IdentifyAsync(PlantIdentificationRequest request, CancellationToken cancellationToken)
        {
            Calls++;
            return _implementation(request, cancellationToken);
        }
    }

    private sealed class FakeKnowledgeProvider : IPlantKnowledgeProvider
    {
        private readonly Func<PlantKnowledgeRequest, CancellationToken, Task<PlantKnowledgeResult?>> _implementation;

        public FakeKnowledgeProvider(Func<PlantKnowledgeRequest, CancellationToken, Task<PlantKnowledgeResult?>>? implementation = null) =>
            _implementation = implementation ?? ((_, _) => Task.FromResult<PlantKnowledgeResult?>(null));

        public int Calls { get; private set; }

        public Task<PlantKnowledgeResult?> GetKnowledgeAsync(PlantKnowledgeRequest request, CancellationToken cancellationToken)
        {
            Calls++;
            return _implementation(request, cancellationToken);
        }
    }
}
