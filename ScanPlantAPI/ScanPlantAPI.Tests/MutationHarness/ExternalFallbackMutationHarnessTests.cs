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
    public async Task ValidateAsync_WhenPayloadIsExactlyMaxImageBytes_AcceptsIt()
    {
        const int maxImageBytes = 256;
        await using var image = PaddedPng(maxImageBytes, 1, 1);

        var result = await CreateValidator(maxImageBytes: maxImageBytes).ValidateAsync(
            new ExternalFallbackUpload(image, maxImageBytes, "image/png", true));

        var validated = Assert.IsType<ValidatedImage>(result.Image);
        Assert.Equal(ExternalFallbackUploadFailure.None, result.Failure);
        Assert.Equal(maxImageBytes, validated.Content.Length);
    }

    [Fact]
    public async Task ValidateAsync_WhenDimensionsAreExactlyAtLimit_AcceptsIt()
    {
        await using var image = Png(2, 2);

        var result = await CreateValidator(maxImageDimension: 2).ValidateAsync(
            new ExternalFallbackUpload(image, image.Length, "image/png", true));

        var validated = Assert.IsType<ValidatedImage>(result.Image);
        Assert.Equal(ExternalFallbackUploadFailure.None, result.Failure);
        Assert.Equal(2, validated.Width);
        Assert.Equal(2, validated.Height);
    }

    [Fact]
    public async Task ValidateAsync_WhenPayloadIsFragmentedExactlyAtLimit_PreservesBytesAndUsesBoundedReads()
    {
        const int maxImageBytes = 256;
        var expected = PaddedPng(maxImageBytes, 1, 1).ToArray();
        await using var image = new FragmentedReadStream(expected, maxFragmentSize: 17, maxRequestedBufferLength: maxImageBytes + 1);

        var result = await CreateValidator(maxImageBytes: maxImageBytes).ValidateAsync(
            new ExternalFallbackUpload(image, maxImageBytes, "image/png", true));

        var validated = Assert.IsType<ValidatedImage>(result.Image);
        Assert.Equal(ExternalFallbackUploadFailure.None, result.Failure);
        Assert.Equal(expected, validated.Content);
        Assert.InRange(image.LargestRequestedBufferLength, 1, maxImageBytes + 1);
    }

    [Fact]
    public async Task ValidateAsync_WhenActualPayloadHasFirstByteOverLimitDespiteDeclaredLength_RejectsIt()
    {
        const int maxImageBytes = 256;
        await using var image = new FragmentedReadStream(PaddedPng(maxImageBytes + 1, 1, 1).ToArray(), maxFragmentSize: 31);

        var result = await CreateValidator(maxImageBytes: maxImageBytes).ValidateAsync(
            new ExternalFallbackUpload(image, maxImageBytes, "image/png", true));

        Assert.Equal(ExternalFallbackUploadFailure.PayloadTooLarge, result.Failure);
        Assert.False(result.IsValid);
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

    private static ExternalFallbackUploadValidator CreateValidator(int maxImageDimension = 4096, int maxImageBytes = 20 * 1024) =>
        new(Options.Create(CreateOptions(maxImageDimension, maxImageBytes: maxImageBytes)));

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

    private static ExternalFallbackOptions CreateOptions(int maxImageDimension, int requestTimeoutSeconds = 20, int maxImageBytes = 20 * 1024) => new()
    {
        MaxImageBytes = maxImageBytes,
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

    private static MemoryStream PaddedPng(int length, uint width, uint height)
    {
        var bytes = Png(width, height).ToArray();
        Assert.True(bytes.Length <= length);
        Array.Resize(ref bytes, length);
        return new MemoryStream(bytes);
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

    private sealed class FragmentedReadStream : Stream
    {
        private readonly MemoryStream _source;
        private readonly int _maxFragmentSize;
        private readonly int? _maxRequestedBufferLength;

        public FragmentedReadStream(byte[] content, int maxFragmentSize, int? maxRequestedBufferLength = null)
        {
            _source = new MemoryStream(content);
            _maxFragmentSize = maxFragmentSize;
            _maxRequestedBufferLength = maxRequestedBufferLength;
        }

        public int LargestRequestedBufferLength { get; private set; }

        public override bool CanRead => true;
        public override bool CanSeek => false;
        public override bool CanWrite => false;
        public override long Length => throw new NotSupportedException();
        public override long Position { get => throw new NotSupportedException(); set => throw new NotSupportedException(); }

        public override int Read(byte[] buffer, int offset, int count) =>
            ReadAsync(buffer.AsMemory(offset, count), CancellationToken.None).GetAwaiter().GetResult();

        public override ValueTask<int> ReadAsync(Memory<byte> buffer, CancellationToken cancellationToken = default)
        {
            LargestRequestedBufferLength = Math.Max(LargestRequestedBufferLength, buffer.Length);
            if (_maxRequestedBufferLength is not null && buffer.Length > _maxRequestedBufferLength)
            {
                throw new InvalidOperationException("The validator requested an unbounded read buffer.");
            }

            return _source.ReadAsync(buffer[..Math.Min(buffer.Length, _maxFragmentSize)], cancellationToken);
        }

        public override void Flush() => throw new NotSupportedException();
        public override long Seek(long offset, SeekOrigin origin) => throw new NotSupportedException();
        public override void SetLength(long value) => throw new NotSupportedException();
        public override void Write(byte[] buffer, int offset, int count) => throw new NotSupportedException();

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                _source.Dispose();
            }

            base.Dispose(disposing);
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
