using Microsoft.Extensions.Options;

namespace ScanPlantAPI.Services.ExternalProviders;

internal sealed class ExternalFallbackOptions
{
    public const string SectionName = "ExternalFallback";

    public long MaxImageBytes { get; set; } = 5 * 1024 * 1024;
    public int MaxImageWidth { get; set; } = 4096;
    public int MaxImageHeight { get; set; } = 4096;
    public int RequestTimeoutSeconds { get; set; } = 20;
    public int RateLimitPermitLimit { get; set; } = 10;
    public int RateLimitWindowSeconds { get; set; } = 60;
    public string[] AllowedMediaTypes { get; set; } = ["image/jpeg", "image/png"];
}

internal sealed class ExternalFallbackOptionsValidator : IValidateOptions<ExternalFallbackOptions>
{
    public ValidateOptionsResult Validate(string? name, ExternalFallbackOptions options)
    {
        var failures = new List<string>();

        if (options.MaxImageBytes <= 0 || options.MaxImageBytes >= int.MaxValue)
        {
            failures.Add("ExternalFallback:MaxImageBytes deve ser maior que zero.");
        }

        if (options.MaxImageWidth <= 0 || options.MaxImageHeight <= 0)
        {
            failures.Add("ExternalFallback:MaxImageWidth e MaxImageHeight devem ser maiores que zero.");
        }

        if (options.RequestTimeoutSeconds <= 0)
        {
            failures.Add("ExternalFallback:RequestTimeoutSeconds deve ser maior que zero.");
        }

        if (options.RateLimitPermitLimit <= 0 || options.RateLimitWindowSeconds <= 0)
        {
            failures.Add("Os limites de taxa do fallback externo devem ser maiores que zero.");
        }

        var allowedMediaTypes = options.AllowedMediaTypes ?? [];
        if (allowedMediaTypes.Length == 0 || allowedMediaTypes.Any(string.IsNullOrWhiteSpace))
        {
            failures.Add("ExternalFallback:AllowedMediaTypes deve conter pelo menos um MIME válido.");
        }

        return failures.Count == 0 ? ValidateOptionsResult.Success : ValidateOptionsResult.Fail(failures);
    }
}

internal static class ExternalProviderClientNames
{
    public const string PlantNet = "ExternalFallback.PlantNet";
    public const string Groq = "ExternalFallback.Groq";
}

internal static class ExternalFallbackRateLimitPolicy
{
    public const string Name = "external-fallback-per-user";
}
