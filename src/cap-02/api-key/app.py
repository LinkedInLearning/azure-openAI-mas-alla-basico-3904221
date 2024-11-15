from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2023-03-15-preview",
    azure_endpoint="https://azure-openai-avanzado.openai.azure.com/",
    api_key="AM9pc0PPqNCAThXPxqvgw8zFHOi0UWgleVlnUlXfNd4xkCIxuw1CJQQJ99AKACfhMk5XJ3w3AAABACOGYSdn"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Eres un asistente muy útil."},
        {"role": "user", "content": "Cuáles son las características principales de los perros Beagle?"},
    ]
)

print(response.choices[0].message.content)