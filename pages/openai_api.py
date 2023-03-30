import requests

def generate_answer(prompt, api_key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {'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'}'
    }
    data = {
        "prompt": prompt,
        "model": "text-davinci-002",
        "max_tokens":100,
        "stop":"."
    }

    resp = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate answer "+resp.text)

    return resp.json()['choices'][0]['text']



import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Correct this to standard English:\n\nShe no went to the market.",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)



