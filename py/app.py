import os
import openai
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def hello_world():
    prompt = "Hello, GPT-3!"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

if __name__ == '__main__':
    app.run()
