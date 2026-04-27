# pip install google-genai
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

print("List of models that support generateContent:\n")
for m in client.models.list():
    for action in m.supported_actions:
        if action == "generateContent":
            print(m.name)

model = "gemini-flash-lite-latest"
try:
    response = client.models.generate_content(
        model=model,
        contents="Invent an original joke that non-English speakers could understand"
        # contents="תמציא בדיחה מקורית"
    )
    print(response.text)
except genai.errors.ServerError as err:
    print(f"Model {model} error: {err}")
