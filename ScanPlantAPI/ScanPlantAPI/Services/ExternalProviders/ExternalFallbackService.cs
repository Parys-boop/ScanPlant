using Microsoft.Extensions.Options;

namespace ScanPlantAPI.Services.ExternalProviders;

internal interface IExternalFallbackService
{
    Task<ExternalFallbackServiceResult> ExecuteAsync(ExternalFallbackUpload upload, CancellationToken requestAborted);
}

internal sealed record ExternalFallbackServiceResult(
    ExternalFallbackUploadFailure UploadFailure,
    ExternalFallbackResult? Result,
    string KnowledgeStatus,
    ExternalProviderRateLimitException? RateLimitException = null,
    ExternalProviderUnavailableException? UnavailableException = null,
    bool TimedOut = false);

internal sealed class ExternalFallbackService : IExternalFallbackService
{
    private readonly ExternalFallbackUploadValidator _uploadValidator;
    private readonly IPlantIdentificationProvider _identificationProvider;
    private readonly IPlantKnowledgeProvider _knowledgeProvider;
    private readonly ExternalFallbackOptions _options;
    private readonly IConfiguration _configuration;
    private readonly ILogger<ExternalFallbackService> _logger;

    public ExternalFallbackService(
        ExternalFallbackUploadValidator uploadValidator,
        IPlantIdentificationProvider identificationProvider,
        IPlantKnowledgeProvider knowledgeProvider,
        IOptions<ExternalFallbackOptions> options,
        IConfiguration configuration,
        ILogger<ExternalFallbackService> logger)
    {
        _uploadValidator = uploadValidator;
        _identificationProvider = identificationProvider;
        _knowledgeProvider = knowledgeProvider;
        _options = options.Value;
        _configuration = configuration;
        _logger = logger;
    }

    public async Task<ExternalFallbackServiceResult> ExecuteAsync(ExternalFallbackUpload upload, CancellationToken requestAborted)
    {
        var validation = await _uploadValidator.ValidateAsync(upload, requestAborted);
        if (!validation.IsValid)
        {
            return new ExternalFallbackServiceResult(validation.Failure, null, "not_requested");
        }

        using var timeout = CancellationTokenSource.CreateLinkedTokenSource(requestAborted);
        timeout.CancelAfter(TimeSpan.FromSeconds(_options.RequestTimeoutSeconds));
        try
        {
            var identification = await _identificationProvider.IdentifyAsync(new PlantIdentificationRequest(validation.Image!), timeout.Token);
            if (identification.Candidates.Count == 0)
            {
                return new ExternalFallbackServiceResult(ExternalFallbackUploadFailure.None, new ExternalFallbackResult(identification, null), "not_requested");
            }

            var selected = NormalizeScientificName(identification.Candidates[0].ScientificName);
            if (!KnowledgeEnabled())
            {
                return new ExternalFallbackServiceResult(ExternalFallbackUploadFailure.None, new ExternalFallbackResult(identification, null), "not_requested");
            }

            try
            {
                var knowledge = await _knowledgeProvider.GetKnowledgeAsync(new PlantKnowledgeRequest(selected), timeout.Token);
                return new ExternalFallbackServiceResult(
                    ExternalFallbackUploadFailure.None,
                    new ExternalFallbackResult(identification, knowledge),
                    knowledge is null ? "unavailable" : "available");
            }
            catch (OperationCanceledException) when (requestAborted.IsCancellationRequested)
            {
                throw;
            }
            catch (OperationCanceledException) when (timeout.IsCancellationRequested)
            {
                return new ExternalFallbackServiceResult(ExternalFallbackUploadFailure.None, new ExternalFallbackResult(identification, null), "timeout");
            }
            catch (Exception exception)
            {
                _logger.LogWarning("External fallback knowledge provider failed with {ProviderStatus}", exception.GetType().Name);
                return new ExternalFallbackServiceResult(ExternalFallbackUploadFailure.None, new ExternalFallbackResult(identification, null), "failed");
            }
        }
        catch (OperationCanceledException) when (requestAborted.IsCancellationRequested)
        {
            throw;
        }
        catch (OperationCanceledException) when (timeout.IsCancellationRequested)
        {
            return new ExternalFallbackServiceResult(ExternalFallbackUploadFailure.None, null, "not_requested", TimedOut: true);
        }
        catch (ExternalProviderRateLimitException exception)
        {
            return new ExternalFallbackServiceResult(ExternalFallbackUploadFailure.None, null, "not_requested", RateLimitException: exception);
        }
        catch (ExternalProviderUnavailableException exception)
        {
            return new ExternalFallbackServiceResult(ExternalFallbackUploadFailure.None, null, "not_requested", UnavailableException: exception);
        }
        catch (HttpRequestException exception)
        {
            return new ExternalFallbackServiceResult(
                ExternalFallbackUploadFailure.None,
                null,
                "not_requested",
                UnavailableException: new ExternalProviderUnavailableException("plantnet", StatusCodes.Status503ServiceUnavailable, exception));
        }
    }

    private bool KnowledgeEnabled() => _configuration.GetValue<bool>("Groq:Enabled");

    private static string NormalizeScientificName(string scientificName) =>
        string.Join(' ', scientificName.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries));
}
