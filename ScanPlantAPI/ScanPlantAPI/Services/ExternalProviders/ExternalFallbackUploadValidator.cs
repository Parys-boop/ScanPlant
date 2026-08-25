using Microsoft.Extensions.Options;
using SkiaSharp;

namespace ScanPlantAPI.Services.ExternalProviders;

internal sealed record ExternalFallbackUpload(Stream? Content, long? DeclaredLength, string? ContentType, bool ConsentToExternalProcessing);

internal enum ExternalFallbackUploadFailure
{
    None,
    MissingImage,
    ConsentRequired,
    PayloadTooLarge,
    UnsupportedMediaType,
    InvalidImageSignature,
    InvalidImageDimensions
}

internal sealed record ValidatedImage(byte[] Content, string ContentType, int Width, int Height)
{
    public Stream OpenReadStream() => new MemoryStream(Content, writable: false);
}

internal sealed record ExternalFallbackUploadValidationResult(ValidatedImage? Image, ExternalFallbackUploadFailure Failure)
{
    public bool IsValid => Image is not null && Failure == ExternalFallbackUploadFailure.None;
}

internal sealed class ExternalFallbackUploadValidator
{
    private readonly ExternalFallbackOptions _options;

    public ExternalFallbackUploadValidator(IOptions<ExternalFallbackOptions> options)
    {
        _options = options.Value;
    }

    public async Task<ExternalFallbackUploadValidationResult> ValidateAsync(
        ExternalFallbackUpload upload,
        CancellationToken cancellationToken = default)
    {
        if (upload.Content is null || !upload.Content.CanRead || upload.DeclaredLength is <= 0)
        {
            return Failure(ExternalFallbackUploadFailure.MissingImage);
        }

        if (!upload.ConsentToExternalProcessing)
        {
            return Failure(ExternalFallbackUploadFailure.ConsentRequired);
        }

        if (upload.DeclaredLength > _options.MaxImageBytes)
        {
            return Failure(ExternalFallbackUploadFailure.PayloadTooLarge);
        }

        var contentType = upload.ContentType?.Trim().ToLowerInvariant();
        if (string.IsNullOrWhiteSpace(contentType) ||
            !_options.AllowedMediaTypes.Contains(contentType, StringComparer.OrdinalIgnoreCase))
        {
            return Failure(ExternalFallbackUploadFailure.UnsupportedMediaType);
        }

        var content = await ReadWithinLimitAsync(upload.Content, _options.MaxImageBytes, cancellationToken);
        if (content is null)
        {
            return Failure(ExternalFallbackUploadFailure.PayloadTooLarge);
        }

        using var encoded = SKData.CreateCopy(content);
        using var codec = SKCodec.Create(encoded);
        if (codec is null || !TryGetContentType(codec.EncodedFormat, out var detectedContentType) ||
            !string.Equals(contentType, detectedContentType, StringComparison.OrdinalIgnoreCase))
        {
            return Failure(ExternalFallbackUploadFailure.InvalidImageSignature);
        }

        var imageInfo = codec.Info;
        if (imageInfo.Width <= 0 || imageInfo.Height <= 0 ||
            imageInfo.Width > _options.MaxImageWidth || imageInfo.Height > _options.MaxImageHeight)
        {
            return Failure(ExternalFallbackUploadFailure.InvalidImageDimensions);
        }

        using var bitmap = new SKBitmap(imageInfo);
        if (codec.GetPixels(bitmap.Info, bitmap.GetPixels()) != SKCodecResult.Success)
        {
            return Failure(ExternalFallbackUploadFailure.InvalidImageSignature);
        }

        return new ExternalFallbackUploadValidationResult(
            new ValidatedImage(content, detectedContentType, imageInfo.Width, imageInfo.Height),
            ExternalFallbackUploadFailure.None);
    }

    private static ExternalFallbackUploadValidationResult Failure(ExternalFallbackUploadFailure failure) => new(null, failure);

    private static async Task<byte[]?> ReadWithinLimitAsync(Stream content, long maxBytes, CancellationToken cancellationToken)
    {
        var maximumBufferLength = checked((int)Math.Min(maxBytes + 1, int.MaxValue));
        await using var buffer = new MemoryStream(capacity: maximumBufferLength);
        var chunk = new byte[Math.Min(81920, maximumBufferLength)];
        int read;

        while ((read = await content.ReadAsync(chunk.AsMemory(), cancellationToken)) > 0)
        {
            if (buffer.Length + read > maxBytes)
            {
                return null;
            }

            await buffer.WriteAsync(chunk.AsMemory(0, read), cancellationToken);
        }

        return buffer.Length == 0 ? null : buffer.ToArray();
    }

    private static bool TryGetContentType(SKEncodedImageFormat format, out string contentType)
    {
        contentType = format switch
        {
            SKEncodedImageFormat.Png => "image/png",
            SKEncodedImageFormat.Jpeg => "image/jpeg",
            _ => string.Empty
        };
        return contentType.Length > 0;
    }
}
