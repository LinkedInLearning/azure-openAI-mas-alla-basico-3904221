using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Extensions.OpenAI.TextCompletion;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace DogBreeds;

public class DogBreedsFunction(ILogger<DogBreedsFunction> logger)
{
    [Function(nameof(DogBreedsFunction))]
    public async Task<HttpResponseData> Run([HttpTrigger(AuthorizationLevel.Function, "get", Route = "breeds/{breed}")] 
                                HttpRequestData req,
                            [TextCompletionInput("Dame las 10 características más importantes de la raza de perros: {breed}",
                                        MaxTokens = "1000",
                                        Temperature = "0,7",
                                        Model = "%MODEL_NAME%")] TextCompletionResponse response)
    {
        logger.LogInformation($"Total de tokens: {response.TotalTokens}");

        var data = req.CreateResponse(System.Net.HttpStatusCode.OK);

        await data.WriteStringAsync(response.Content);

        return data;
    }
}