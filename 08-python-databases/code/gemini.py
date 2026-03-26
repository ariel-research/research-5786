from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents="Invent an original joke that non-English speakers could understand"
)
print(response.text)
