using Microsoft.Extensions.Options;
using ScanPlantAPI.Services.ExternalProviders;
using System.Buffers.Binary;
using System.IO.Compression;

namespace ScanPlantAPI.Tests;

public sealed class ExternalFallbackUploadValidatorTests
{
    private readonly ExternalFallbackUploadValidator _validator = CreateValidator();

    private static ExternalFallbackUploadValidator CreateValidator(int maxImageDimension = 4096) => new(Options.Create(new ExternalFallbackOptions
    {
        MaxImageBytes = 20 * 1024,
        MaxImageWidth = maxImageDimension,
        MaxImageHeight = maxImageDimension,
        AllowedMediaTypes = ["image/png", "image/jpeg"]
    }));

    [Fact]
    public async Task ValidateAsync_WhenImageIsMissing_ReturnsMissingImage()
    {
        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(null, null, null, true));

        Assert.Equal(ExternalFallbackUploadFailure.MissingImage, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenExternalConsentIsFalse_ReturnsConsentRequired()
    {
        await using var image = Png(1, 1);

        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/png", false));

        Assert.Equal(ExternalFallbackUploadFailure.ConsentRequired, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenImageExceedsTheConfiguredLimit_ReturnsPayloadTooLarge()
    {
        await using var image = new MemoryStream(new byte[20 * 1024 + 1]);

        var result = await CreateValidator(4).ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/png", true));

        Assert.Equal(ExternalFallbackUploadFailure.PayloadTooLarge, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenMimeTypeIsNotAllowed_ReturnsUnsupportedMediaType()
    {
        await using var image = Png(1, 1);

        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/gif", true));

        Assert.Equal(ExternalFallbackUploadFailure.UnsupportedMediaType, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenSignatureDoesNotMatchMimeType_ReturnsInvalidSignature()
    {
        await using var image = Jpeg(1, 1);

        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/png", true));

        Assert.Equal(ExternalFallbackUploadFailure.InvalidImageSignature, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenPngIsTruncated_ReturnsInvalidSignature()
    {
        await using var validImage = Png(1, 1);
        await using var truncatedImage = new MemoryStream(validImage.ToArray()[..24]);

        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(truncatedImage, truncatedImage.Length, "image/png", true));

        Assert.Equal(ExternalFallbackUploadFailure.InvalidImageSignature, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenJpegIsValid_ReturnsTransientValidatedImage()
    {
        await using var image = OpenJpegFixture();

        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/jpeg", true));

        var validatedImage = Assert.IsType<ValidatedImage>(result.Image);
        Assert.Equal("image/jpeg", validatedImage.ContentType);
        Assert.True(validatedImage.Width > 0);
        Assert.True(validatedImage.Height > 0);
    }

    [Fact]
    public async Task ValidateAsync_WhenJpegIsTruncated_ReturnsInvalidSignature()
    {
        await using var fixture = OpenJpegFixture();
        var bytes = fixture.ToArray();
        await using var image = new MemoryStream(bytes[..^2]);

        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/jpeg", true));

        Assert.Equal(ExternalFallbackUploadFailure.InvalidImageSignature, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenDimensionsExceedTheConfiguredLimit_ReturnsInvalidDimensions()
    {
        await using var image = Png(5, 1);

        var result = await CreateValidator(4).ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/png", true));

        Assert.Equal(ExternalFallbackUploadFailure.InvalidImageDimensions, result.Failure);
    }

    [Fact]
    public async Task ValidateAsync_WhenPngIsValid_ReturnsTransientValidatedImage()
    {
        await using var image = Png(2, 3);

        var result = await _validator.ValidateAsync(new ExternalFallbackUpload(image, image.Length, "image/png", true));

        var validatedImage = Assert.IsType<ValidatedImage>(result.Image);
        Assert.Equal("image/png", validatedImage.ContentType);
        Assert.Equal(2, validatedImage.Width);
        Assert.Equal(3, validatedImage.Height);
    }

    private static MemoryStream Png(uint width, uint height)
    {
        using var output = new MemoryStream();
        output.Write([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]);

        var header = new byte[13];
        WriteUInt32BigEndian(header, 0, width);
        WriteUInt32BigEndian(header, 4, height);
        header[8] = 8;
        header[9] = 6;
        WriteChunk(output, "IHDR"u8, header);

        var rawPixels = new byte[checked((int)(height * (width * 4 + 1)))];
        using var compressedData = new MemoryStream();
        using (var zlib = new ZLibStream(compressedData, CompressionLevel.SmallestSize, leaveOpen: true))
        {
            zlib.Write(rawPixels);
        }

        WriteChunk(output, "IDAT"u8, compressedData.ToArray());
        WriteChunk(output, "IEND"u8, []);
        return new MemoryStream(output.ToArray());
    }

    private static MemoryStream Jpeg(ushort width, ushort height)
    {
        return new MemoryStream([
            0xFF, 0xD8, 0xFF, 0xC0, 0x00, 0x08, 0x08,
            (byte)(height >> 8), (byte)height, (byte)(width >> 8), (byte)width, 0x01
        ]);
    }

    private static MemoryStream OpenJpegFixture() => new(File.ReadAllBytes(Path.Combine(AppContext.BaseDirectory, "Fixtures", "daisy.jpg")));

    private static void WriteUInt32BigEndian(byte[] bytes, int offset, uint value)
    {
        bytes[offset] = (byte)(value >> 24);
        bytes[offset + 1] = (byte)(value >> 16);
        bytes[offset + 2] = (byte)(value >> 8);
        bytes[offset + 3] = (byte)value;
    }

    private static void WriteChunk(Stream output, ReadOnlySpan<byte> type, ReadOnlySpan<byte> data)
    {
        Span<byte> length = stackalloc byte[4];
        BinaryPrimitives.WriteUInt32BigEndian(length, (uint)data.Length);
        output.Write(length);
        output.Write(type);
        output.Write(data);
        BinaryPrimitives.WriteUInt32BigEndian(length, CalculateCrc(type, data));
        output.Write(length);
    }

    private static uint CalculateCrc(ReadOnlySpan<byte> type, ReadOnlySpan<byte> data)
    {
        var crc = 0xFFFFFFFFu;
        foreach (var value in type)
        {
            crc = UpdateCrc(crc, value);
        }

        foreach (var value in data)
        {
            crc = UpdateCrc(crc, value);
        }

        return ~crc;
    }

    private static uint UpdateCrc(uint crc, byte value)
    {
        crc ^= value;
        for (var bit = 0; bit < 8; bit++)
        {
            crc = (crc >> 1) ^ ((crc & 1) == 1 ? 0xEDB88320u : 0);
        }

        return crc;
    }
}
