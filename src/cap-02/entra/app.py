from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    api_version="2023-03-15-preview",
    azure_endpoint="https://azure-openai-avanzado.openai.azure.com/",
    azure_ad_token_provider=token_provider
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Eres un asistente muy útil."},
        {"role": "user", "content": "Cuáles son las características principales de los perros Beagle?"},
    ]
)

print(response.choices[0].message.content)