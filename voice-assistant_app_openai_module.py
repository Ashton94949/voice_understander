import openai

# Set up your OpenAI API key
openai.api_key = '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'

def query_openai(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()
