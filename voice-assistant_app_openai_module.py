import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def query_openai(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()