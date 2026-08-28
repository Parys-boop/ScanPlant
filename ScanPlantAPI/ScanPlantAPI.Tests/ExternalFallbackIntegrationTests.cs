#if NET10_0_OR_GREATER
using System.Collections.Concurrent;
using System.IdentityModel.Tokens.Jwt;
using System.Net;
using System.Net.Http.Headers;
using System.Security.Claims;
using System.Text;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using ScanPlantAPI.Services.ExternalProviders;

namespace ScanPlantAPI.Tests;

public sealed class ExternalFallbackIntegrationTests
{
    private const string JwtKey = "fallback-integration-test-key-which-is-not-a-secret";

    [Fact]
    public async Task Fallback_WithoutAuthentication_Returns401WithoutCallingAProvider()
    {
        var state = new FallbackTestState();
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await client.PostAsync("/api/plant-identification/fallback", CreateUpload(true));

        Assert.Equal(HttpStatusCode.Unauthorized, response.StatusCode);
        Assert.Equal(0, state.IdentificationCalls);
    }

    [Theory]
    [InlineData(null)]
    [InlineData(false)]
    public async Task Fallback_WithoutExplicitConsent_Returns400WithoutCallingAProvider(bool? consent)
    {
        var state = new FallbackTestState();
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await PostAuthorizedAsync(client, CreateUpload(consent));

        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
        Assert.Equal(0, state.IdentificationCalls);
    }

    [Fact]
    public async Task Fallback_WhenUploadedFileIsEmpty_ReturnsNeutral400WithoutCallingAProvider()
    {
        var state = new FallbackTestState();
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await PostAuthorizedAsync(client, CreateEmptyUpload());

        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
        Assert.NotEqual(HttpStatusCode.RequestEntityTooLarge, response.StatusCode);
        Assert.Equal(0, state.IdentificationCalls);
        var body = await response.Content.ReadAsStringAsync();
        Assert.Contains("A imagem ou o consentimento são inválidos.", body, StringComparison.Ordinal);
        Assert.DoesNotContain("plantnet", body, StringComparison.OrdinalIgnoreCase);
        Assert.DoesNotContain("groq", body, StringComparison.OrdinalIgnoreCase);
    }

    [Fact]
    public async Task Fallback_WhenLocalRateLimitIsExceeded_Returns429()
    {
        var state = new FallbackTestState { RateLimitPermitLimit = 1 };
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var first = await PostAuthorizedAsync(client, CreateUpload(true));
        using var second = await PostAuthorizedAsync(client, CreateUpload(true));

        Assert.Equal(HttpStatusCode.OK, first.StatusCode);
        Assert.Equal(HttpStatusCode.TooManyRequests, second.StatusCode);
        Assert.Equal(1, state.IdentificationCalls);
    }

    [Fact]
    public async Task Fallback_WhenIdentificationTimesOut_ReturnsControlled504WithoutRetry()
    {
        var state = new FallbackTestState
        {
            RequestTimeoutSeconds = 1,
            Identify = async (_, cancellationToken) =>
            {
                await Task.Delay(Timeout.InfiniteTimeSpan, cancellationToken);
                return PlantIdentificationResult.NoMatch;
            }
        };
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await PostAuthorizedAsync(client, CreateUpload(true));

        Assert.Equal(HttpStatusCode.GatewayTimeout, response.StatusCode);
        Assert.Equal(1, state.IdentificationCalls);
        Assert.DoesNotContain("PlantNet", await response.Content.ReadAsStringAsync(), StringComparison.OrdinalIgnoreCase);
    }

    [Fact]
    public async Task Fallback_WhenIdentificationProviderReturns429_PreservesOnlySafeRetryAfter()
    {
        var state = new FallbackTestState
        {
            Identify = (_, _) => throw new ExternalProviderRateLimitException("plantnet", TimeSpan.FromSeconds(5))
        };
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await PostAuthorizedAsync(client, CreateUpload(true));

        Assert.Equal(HttpStatusCode.TooManyRequests, response.StatusCode);
        Assert.Equal("5", response.Headers.RetryAfter?.Delta?.TotalSeconds.ToString(System.Globalization.CultureInfo.InvariantCulture));
        var body = await response.Content.ReadAsStringAsync();
        Assert.DoesNotContain("plantnet", body, StringComparison.OrdinalIgnoreCase);
        Assert.DoesNotContain("provider", body, StringComparison.OrdinalIgnoreCase);
    }

    [Fact]
    public async Task Fallback_WhenGroqFails_ReturnsIdentificationAndDoesNotExposeSensitiveDetails()
    {
        const string simulatedSensitiveValue = "synthetic-groq-secret";
        var state = new FallbackTestState
        {
            GroqEnabled = true,
            Knowledge = (_, _) => throw new HttpRequestException(simulatedSensitiveValue)
        };
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await PostAuthorizedAsync(client, CreateUpload(true));

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        var body = await response.Content.ReadAsStringAsync();
        Assert.Contains("\"knowledgeStatus\":\"failed\"", body, StringComparison.Ordinal);
        Assert.Contains("Ficus lyrata", body, StringComparison.Ordinal);
        Assert.DoesNotContain(simulatedSensitiveValue, body, StringComparison.Ordinal);
        Assert.DoesNotContain(simulatedSensitiveValue, state.Logs.Messages, StringComparer.Ordinal);
    }

    [Fact]
    public async Task Fallback_WithFakeProviders_ReturnsNormalizedExternalFallbackResponse()
    {
        var state = new FallbackTestState
        {
            GroqEnabled = true,
            Knowledge = (_, _) => Task.FromResult<PlantKnowledgeResult?>(new PlantKnowledgeResult("Indirect light", null, null))
        };
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await PostAuthorizedAsync(client, CreateUpload(true));

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        var body = await response.Content.ReadAsStringAsync();
        Assert.Contains("\"source\":\"external_fallback\"", body, StringComparison.Ordinal);
        Assert.Contains("\"matchStatus\":\"identified\"", body, StringComparison.Ordinal);
        Assert.Contains("\"knowledgeStatus\":\"available\"", body, StringComparison.Ordinal);
        Assert.Contains("Ficus lyrata", body, StringComparison.Ordinal);
    }

    [Fact]
    public async Task Fallback_WhenProviderFindsNoMatch_ReturnsNormalNoMatchResponse()
    {
        var state = new FallbackTestState { Identify = (_, _) => Task.FromResult(PlantIdentificationResult.NoMatch) };
        using var factory = new ExternalFallbackFactory(state);
        using var client = factory.CreateClient();

        using var response = await PostAuthorizedAsync(client, CreateUpload(true));

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        var body = await response.Content.ReadAsStringAsync();
        Assert.Contains("\"matchStatus\":\"no_match\"", body, StringComparison.Ordinal);
        Assert.Contains("\"knowledgeStatus\":\"not_requested\"", body, StringComparison.Ordinal);
    }

    private static async Task<HttpResponseMessage> PostAuthorizedAsync(HttpClient client, HttpContent content)
    {
        using var request = new HttpRequestMessage(HttpMethod.Post, "/api/plant-identification/fallback") { Content = content };
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", CreateToken());
        return await client.SendAsync(request);
    }

    private static MultipartFormDataContent CreateUpload(bool? consent)
    {
        var content = new MultipartFormDataContent();
        var image = new ByteArrayContent(File.ReadAllBytes(Path.Combine(AppContext.BaseDirectory, "Fixtures", "daisy.jpg")));
        image.Headers.ContentType = new MediaTypeHeaderValue("image/jpeg");
        content.Add(image, "image", "plant.jpg");
        if (consent is not null)
        {
            content.Add(new StringContent(consent.Value ? "true" : "false"), "consentToExternalProcessing");
        }
        return content;
    }

    private static MultipartFormDataContent CreateEmptyUpload()
    {
        var content = new MultipartFormDataContent();
        var image = new ByteArrayContent([]);
        image.Headers.ContentType = new MediaTypeHeaderValue("image/png");
        content.Add(image, "image", "empty.png");
        content.Add(new StringContent("true"), "consentToExternalProcessing");
        return content;
    }

    private static string CreateToken()
    {
        var credentials = new SigningCredentials(new SymmetricSecurityKey(Encoding.UTF8.GetBytes(JwtKey)), SecurityAlgorithms.HmacSha256);
        var token = new JwtSecurityToken("ScanPlantAPI", "ScanPlantApp", [new Claim(ClaimTypes.NameIdentifier, "integration-user")], null, DateTime.UtcNow.AddMinutes(5), credentials);
        return new JwtSecurityTokenHandler().WriteToken(token);
    }

    private sealed class ExternalFallbackFactory : WebApplicationFactory<Program>
    {
        private readonly FallbackTestState _state;

        public ExternalFallbackFactory(FallbackTestState state)
        {
            _state = state;
            SetTestEnvironment();
        }

        protected override void ConfigureWebHost(IWebHostBuilder builder)
        {
            builder.UseEnvironment("Testing");
            builder.ConfigureAppConfiguration((_, configuration) => configuration.AddInMemoryCollection(new Dictionary<string, string?>
            {
                ["ConnectionStrings:DefaultConnection"] = "Host=unused;Database=unused;Username=unused;Password=unused",
                ["Jwt:Key"] = JwtKey,
                ["Jwt:Issuer"] = "ScanPlantAPI",
                ["Jwt:Audience"] = "ScanPlantApp",
                ["ExternalFallback:RequestTimeoutSeconds"] = _state.RequestTimeoutSeconds.ToString(System.Globalization.CultureInfo.InvariantCulture),
                ["ExternalFallback:RateLimitPermitLimit"] = _state.RateLimitPermitLimit.ToString(System.Globalization.CultureInfo.InvariantCulture),
                ["ExternalFallback:RateLimitWindowSeconds"] = "60",
                ["Groq:Enabled"] = _state.GroqEnabled.ToString()
            }));
            builder.ConfigureServices(services =>
            {
                services.RemoveAll<IPlantIdentificationProvider>();
                services.RemoveAll<IPlantKnowledgeProvider>();
                services.AddSingleton<IPlantIdentificationProvider>(new FakeIdentificationProvider(_state));
                services.AddSingleton<IPlantKnowledgeProvider>(new FakeKnowledgeProvider(_state));
                services.AddSingleton<ILoggerProvider>(_state.Logs);
            });
        }

        private void SetTestEnvironment()
        {
            Environment.SetEnvironmentVariable("ConnectionStrings__DefaultConnection", "Host=unused;Database=unused;Username=unused;Password=unused");
            Environment.SetEnvironmentVariable("Jwt__Key", JwtKey);
            Environment.SetEnvironmentVariable("Jwt__Issuer", "ScanPlantAPI");
            Environment.SetEnvironmentVariable("Jwt__Audience", "ScanPlantApp");
            Environment.SetEnvironmentVariable("ExternalFallback__RequestTimeoutSeconds", _state.RequestTimeoutSeconds.ToString(System.Globalization.CultureInfo.InvariantCulture));
            Environment.SetEnvironmentVariable("ExternalFallback__RateLimitPermitLimit", _state.RateLimitPermitLimit.ToString(System.Globalization.CultureInfo.InvariantCulture));
            Environment.SetEnvironmentVariable("ExternalFallback__RateLimitWindowSeconds", "60");
            Environment.SetEnvironmentVariable("Groq__Enabled", _state.GroqEnabled.ToString());
        }
    }

    private sealed class FallbackTestState
    {
        public int RequestTimeoutSeconds { get; init; } = 20;
        public int RateLimitPermitLimit { get; init; } = 10;
        public bool GroqEnabled { get; init; }
        public int IdentificationCalls;
        public Func<PlantIdentificationRequest, CancellationToken, Task<PlantIdentificationResult>> Identify { get; init; } = (_, _) => Task.FromResult(new PlantIdentificationResult([new PlantIdentificationCandidate("Ficus lyrata", "Fiddle-leaf fig", 0.98m)]));
        public Func<PlantKnowledgeRequest, CancellationToken, Task<PlantKnowledgeResult?>> Knowledge { get; init; } = (_, _) => Task.FromResult<PlantKnowledgeResult?>(null);
        public CapturingLoggerProvider Logs { get; } = new();
    }

    private sealed class FakeIdentificationProvider : IPlantIdentificationProvider
    {
        private readonly FallbackTestState _state;
        public FakeIdentificationProvider(FallbackTestState state) => _state = state;
        public Task<PlantIdentificationResult> IdentifyAsync(PlantIdentificationRequest request, CancellationToken cancellationToken)
        {
            Interlocked.Increment(ref _state.IdentificationCalls);
            return _state.Identify(request, cancellationToken);
        }
    }

    private sealed class FakeKnowledgeProvider : IPlantKnowledgeProvider
    {
        private readonly FallbackTestState _state;
        public FakeKnowledgeProvider(FallbackTestState state) => _state = state;
        public Task<PlantKnowledgeResult?> GetKnowledgeAsync(PlantKnowledgeRequest request, CancellationToken cancellationToken) => _state.Knowledge(request, cancellationToken);
    }

    private sealed class CapturingLoggerProvider : ILoggerProvider
    {
        public ConcurrentBag<string> Messages { get; } = [];
        public ILogger CreateLogger(string categoryName) => new CapturingLogger(Messages);
        public void Dispose() { }

        private sealed class CapturingLogger : ILogger
        {
            private readonly ConcurrentBag<string> _messages;
            public CapturingLogger(ConcurrentBag<string> messages) => _messages = messages;
            public IDisposable? BeginScope<TState>(TState state) where TState : notnull => null;
            public bool IsEnabled(LogLevel logLevel) => true;
            public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception? exception, Func<TState, Exception?, string> formatter)
            {
                _messages.Add(formatter(state, exception));
            }
        }
    }
}
#endif
