using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.RateLimiting;
using Microsoft.Extensions.DependencyInjection;
using ScanPlantAPI.DTOs.Identification;
using ScanPlantAPI.Services.ExternalProviders;

namespace ScanPlantAPI.Controllers;

[ApiController]
[Route("api/plant-identification")]
[Authorize]
public sealed class PlantIdentificationController : ControllerBase
{
    private readonly IExternalFallbackService _service;

    public PlantIdentificationController(IServiceProvider services)
    {
        _service = services.GetRequiredService<IExternalFallbackService>();
    }

    [HttpPost("fallback")]
    [Consumes("multipart/form-data")]
    [EnableRateLimiting(ExternalFallbackRateLimitPolicy.Name)]
    [ProducesResponseType(typeof(ExternalFallbackResponseDto), StatusCodes.Status200OK)]
    public async Task<ActionResult<ExternalFallbackResponseDto>> Fallback(
        [FromForm] IFormFile? image,
        [FromForm] bool consentToExternalProcessing)
    {
        if (Request.Form.Files.Count != 1)
        {
            return BadRequest(Problem(title: "Envie exatamente uma imagem."));
        }

        await using var content = image?.OpenReadStream();
        var outcome = await _service.ExecuteAsync(
            new ExternalFallbackUpload(content, image?.Length, image?.ContentType, consentToExternalProcessing),
            HttpContext.RequestAborted);

        if (outcome.UploadFailure != ExternalFallbackUploadFailure.None)
        {
            return UploadFailure(outcome.UploadFailure);
        }

        if (outcome.RateLimitException is not null)
        {
            if (outcome.RateLimitException.RetryAfter is { } retryAfter)
            {
                Response.Headers.RetryAfter = Math.Ceiling(retryAfter.TotalSeconds).ToString(System.Globalization.CultureInfo.InvariantCulture);
            }
            return StatusCode(StatusCodes.Status429TooManyRequests, Problem(title: "O serviço de identificação está temporariamente limitado."));
        }

        if (outcome.TimedOut)
        {
            return StatusCode(StatusCodes.Status504GatewayTimeout, Problem(title: "O serviço de identificação excedeu o prazo."));
        }

        if (outcome.UnavailableException is not null)
        {
            return StatusCode(outcome.UnavailableException.StatusCode, Problem(title: "O serviço de identificação está indisponível."));
        }

        var result = outcome.Result!;
        return Ok(Map(result, outcome.KnowledgeStatus));
    }

    private ActionResult<ExternalFallbackResponseDto> UploadFailure(ExternalFallbackUploadFailure failure) => failure switch
    {
        ExternalFallbackUploadFailure.PayloadTooLarge => StatusCode(StatusCodes.Status413PayloadTooLarge, Problem(title: "A imagem excede o tamanho permitido.")),
        ExternalFallbackUploadFailure.UnsupportedMediaType or ExternalFallbackUploadFailure.InvalidImageSignature => StatusCode(StatusCodes.Status415UnsupportedMediaType, Problem(title: "O formato da imagem não é aceito.")),
        _ => BadRequest(Problem(title: "A imagem ou o consentimento são inválidos."))
    };

    private static ExternalFallbackResponseDto Map(ExternalFallbackResult result, string knowledgeStatus)
    {
        var candidates = result.Identification.Candidates.Select(candidate => new ExternalPlantCandidateDto
        {
            ScientificName = candidate.ScientificName,
            CommonName = candidate.CommonName,
            Score = candidate.Score
        }).ToArray();
        var first = result.Identification.Candidates.FirstOrDefault();
        return new ExternalFallbackResponseDto
        {
            MatchStatus = first is null ? "no_match" : "identified",
            Identification = first is null ? null : new ExternalPlantIdentificationDto { ScientificName = first.ScientificName, CommonName = first.CommonName },
            Candidates = candidates,
            Knowledge = result.Knowledge is null ? null : new ExternalPlantKnowledgeDto
            {
                CareInstructions = result.Knowledge.CareInstructions,
                Description = result.Knowledge.Description,
                SafetyNotes = result.Knowledge.SafetyNotes
            },
            KnowledgeStatus = knowledgeStatus
        };
    }
}
