using System.Net;
using System.Text.Json;

namespace ScanPlantAPI.Services.ExternalProviders;

internal sealed class PlantNetIdentificationProvider : IPlantIdentificationProvider
{
    private readonly HttpClient _httpClient;
    private readonly IConfiguration _configuration;

    public PlantNetIdentificationProvider(HttpClient httpClient, IConfiguration configuration)
    {
        _httpClient = httpClient;
        _configuration = configuration;
    }

    public async Task<PlantIdentificationResult> IdentifyAsync(PlantIdentificationRequest request, CancellationToken cancellationToken)
    {
        var baseUrl = _configuration["PlantNet:BaseUrl"];
        var apiKey = _configuration["PlantNet:ApiKey"];
        if (string.IsNullOrWhiteSpace(baseUrl) || string.IsNullOrWhiteSpace(apiKey))
        {
            throw new ExternalProviderUnavailableException("plantnet", StatusCodes.Status503ServiceUnavailable);
        }

        var endpoint = new Uri(new Uri(baseUrl, UriKind.Absolute), $"v2/identify/all?api-key={Uri.EscapeDataString(apiKey)}");
        using var stream = request.Image.OpenReadStream();
        using var image = new StreamContent(stream);
        image.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue(request.Image.ContentType);
        using var content = new MultipartFormDataContent();
        content.Add(image, "images", "image");
        using var response = await _httpClient.PostAsync(endpoint, content, cancellationToken);

        if (response.StatusCode == HttpStatusCode.TooManyRequests)
        {
            throw new ExternalProviderRateLimitException("plantnet", SafeRetryAfter(response));
        }

        if (!response.IsSuccessStatusCode)
        {
            throw new ExternalProviderUnavailableException(
                "plantnet",
                (int)response.StatusCode >= 500 ? StatusCodes.Status503ServiceUnavailable : StatusCodes.Status502BadGateway);
        }

        try
        {
            await using var body = await response.Content.ReadAsStreamAsync(cancellationToken);
            using var document = await JsonDocument.ParseAsync(body, cancellationToken: cancellationToken);
            if (!document.RootElement.TryGetProperty("results", out var results) || results.ValueKind != JsonValueKind.Array)
            {
                return PlantIdentificationResult.NoMatch;
            }

            var candidates = new List<PlantIdentificationCandidate>();
            foreach (var result in results.EnumerateArray())
            {
                if (!result.TryGetProperty("species", out var species) || species.ValueKind != JsonValueKind.Object ||
                    !species.TryGetProperty("scientificNameWithoutAuthor", out var nameProperty))
                {
                    continue;
                }

                var scientificName = Normalize(nameProperty.GetString());
                if (scientificName is null)
                {
                    continue;
                }

                string? commonName = null;
                if (species.TryGetProperty("commonNames", out var commonNames) && commonNames.ValueKind == JsonValueKind.Array)
                {
                    commonName = commonNames.EnumerateArray().Select(value => Normalize(value.GetString())).FirstOrDefault(value => value is not null);
                }

                var score = result.TryGetProperty("score", out var scoreProperty) && scoreProperty.TryGetDecimal(out var parsedScore)
                    ? parsedScore
                    : 0m;
                candidates.Add(new PlantIdentificationCandidate(scientificName, commonName, score));
            }

            return candidates.Count == 0 ? PlantIdentificationResult.NoMatch : new PlantIdentificationResult(candidates);
        }
        catch (JsonException exception)
        {
            throw new ExternalProviderUnavailableException("plantnet", StatusCodes.Status502BadGateway, exception);
        }
    }

    private static string? Normalize(string? value)
    {
        var normalized = string.Join(' ', (value ?? string.Empty).Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries));
        return normalized.Length == 0 ? null : normalized;
    }

    private static TimeSpan? SafeRetryAfter(HttpResponseMessage response)
    {
        var retryAfter = response.Headers.RetryAfter?.Delta;
        return retryAfter is not null && retryAfter.Value > TimeSpan.Zero && retryAfter.Value <= TimeSpan.FromHours(1)
            ? retryAfter
            : null;
    }
}
