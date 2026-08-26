namespace ScanPlantAPI.Services.ExternalProviders;

internal sealed class ExternalProviderRateLimitException : Exception
{
    public ExternalProviderRateLimitException(string provider, TimeSpan? retryAfter)
        : base($"O provider {provider} aplicou limite de taxa.")
    {
        Provider = provider;
        RetryAfter = retryAfter;
    }

    public string Provider { get; }
    public TimeSpan? RetryAfter { get; }
}

internal sealed class ExternalProviderUnavailableException : Exception
{
    public ExternalProviderUnavailableException(string provider, int statusCode, Exception? innerException = null)
        : base($"O provider {provider} está indisponível.", innerException)
    {
        Provider = provider;
        StatusCode = statusCode;
    }

    public string Provider { get; }
    public int StatusCode { get; }
}
