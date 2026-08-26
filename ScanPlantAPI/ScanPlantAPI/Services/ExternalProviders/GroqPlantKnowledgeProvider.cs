using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace ScanPlantAPI.Services.ExternalProviders;

internal sealed class GroqPlantKnowledgeProvider : IPlantKnowledgeProvider
{
    private readonly HttpClient _httpClient;
    private readonly IConfiguration _configuration;

    public GroqPlantKnowledgeProvider(HttpClient httpClient, IConfiguration configuration)
    {
        _httpClient = httpClient;
        _configuration = configuration;
    }

    public async Task<PlantKnowledgeResult?> GetKnowledgeAsync(PlantKnowledgeRequest request, CancellationToken cancellationToken)
    {
        var baseUrl = _configuration["Groq:BaseUrl"];
        var apiKey = _configuration["Groq:ApiKey"];
        var model = _configuration["Groq:Model"];
        if (string.IsNullOrWhiteSpace(baseUrl) || string.IsNullOrWhiteSpace(apiKey) || string.IsNullOrWhiteSpace(model))
        {
            throw new ExternalProviderUnavailableException("groq", StatusCodes.Status503ServiceUnavailable);
        }

        var endpoint = new Uri(new Uri(baseUrl, UriKind.Absolute), "openai/v1/chat/completions");
        var payload = JsonSerializer.Serialize(new
        {
            model,
            messages = new[] { new { role = "user", content = $"Forneça cuidados concisos para {request.ScientificName}." } },
            temperature = 0.2
        });
        using var requestMessage = new HttpRequestMessage(HttpMethod.Post, endpoint)
        {
            Content = new StringContent(payload, Encoding.UTF8, "application/json")
        };
        requestMessage.Headers.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);
        using var response = await _httpClient.SendAsync(requestMessage, cancellationToken);

        if (response.StatusCode == HttpStatusCode.TooManyRequests)
        {
            throw new ExternalProviderRateLimitException("groq", null);
        }

        if (!response.IsSuccessStatusCode)
        {
            throw new ExternalProviderUnavailableException(
                "groq",
                (int)response.StatusCode >= 500 ? StatusCodes.Status503ServiceUnavailable : StatusCodes.Status502BadGateway);
        }

        try
        {
            await using var body = await response.Content.ReadAsStreamAsync(cancellationToken);
            using var document = await JsonDocument.ParseAsync(body, cancellationToken: cancellationToken);
            var content = document.RootElement.GetProperty("choices")[0].GetProperty("message").GetProperty("content").GetString();
            return string.IsNullOrWhiteSpace(content) ? null : new PlantKnowledgeResult(content.Trim(), null, null);
        }
        catch (JsonException exception)
        {
            throw new ExternalProviderUnavailableException("groq", StatusCodes.Status502BadGateway, exception);
        }
        catch (KeyNotFoundException exception)
        {
            throw new ExternalProviderUnavailableException("groq", StatusCodes.Status502BadGateway, exception);
        }
        catch (IndexOutOfRangeException exception)
        {
            throw new ExternalProviderUnavailableException("groq", StatusCodes.Status502BadGateway, exception);
        }
    }
}
