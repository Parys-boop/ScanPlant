using System.Net;
using System.Net.Http.Headers;
using Microsoft.Extensions.Configuration;
using ScanPlantAPI.Services.ExternalProviders;

namespace ScanPlantAPI.Tests;

public sealed class ExternalProviderAdapterTests
{
    [Fact]
    public async Task PlantNetProvider_Maps429FromASimulatedHandlerToASafeRetryAfter()
    {
        var handler = new StubHttpMessageHandler(_ =>
        {
            var response = new HttpResponseMessage(HttpStatusCode.TooManyRequests);
            response.Headers.RetryAfter = new RetryConditionHeaderValue(TimeSpan.FromSeconds(5));
            return response;
        });
        var configuration = new ConfigurationBuilder().AddInMemoryCollection(new Dictionary<string, string?>
        {
            ["PlantNet:BaseUrl"] = "https://simulated.invalid/",
            ["PlantNet:ApiKey"] = "synthetic-test-key"
        }).Build();
        var provider = new PlantNetIdentificationProvider(new HttpClient(handler), configuration);

        var exception = await Assert.ThrowsAsync<ExternalProviderRateLimitException>(() => provider.IdentifyAsync(Request(), CancellationToken.None));

        Assert.Equal(TimeSpan.FromSeconds(5), exception.RetryAfter);
        Assert.Equal(1, handler.CallCount);
    }

    [Fact]
    public async Task PlantNetProvider_DropsUnsafeRetryAfterFromASimulatedHandler()
    {
        var handler = new StubHttpMessageHandler(_ =>
        {
            var response = new HttpResponseMessage(HttpStatusCode.TooManyRequests);
            response.Headers.RetryAfter = new RetryConditionHeaderValue(TimeSpan.FromHours(2));
            return response;
        });
        var configuration = new ConfigurationBuilder().AddInMemoryCollection(new Dictionary<string, string?>
        {
            ["PlantNet:BaseUrl"] = "https://simulated.invalid/",
            ["PlantNet:ApiKey"] = "synthetic-test-key"
        }).Build();
        var provider = new PlantNetIdentificationProvider(new HttpClient(handler), configuration);

        var exception = await Assert.ThrowsAsync<ExternalProviderRateLimitException>(() => provider.IdentifyAsync(Request(), CancellationToken.None));

        Assert.Null(exception.RetryAfter);
        Assert.Equal(1, handler.CallCount);
    }

    private static PlantIdentificationRequest Request() => new(new ValidatedImage([137, 80, 78, 71], "image/png", 1, 1));

    private sealed class StubHttpMessageHandler : HttpMessageHandler
    {
        private readonly Func<HttpRequestMessage, HttpResponseMessage> _response;
        public int CallCount { get; private set; }
        public StubHttpMessageHandler(Func<HttpRequestMessage, HttpResponseMessage> response) => _response = response;

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            CallCount++;
            return Task.FromResult(_response(request));
        }
    }
}
