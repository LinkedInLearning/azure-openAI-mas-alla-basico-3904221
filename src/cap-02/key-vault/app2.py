from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI

credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://azure-openai-avanzado-kv.vault.azure.net/", credential=credential)

api_key=client.get_secret("apikey").value

client = AzureOpenAI(
    api_version="2024-02-15-preview",
    azure_endpoint="https://azure-openai-avanzado-eastus.openai.azure.com/",
    api_key=api_key
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Eres un asistente muy útil."},
        {"role": "user", "content": "Cuáles son las características principales de los perros Beagle?"},
    ]
)

print(response.choices[0].message.content)
