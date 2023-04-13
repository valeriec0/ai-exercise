import os
import openai
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

def create_github_issue(title, body):
    # Set the API endpoint for creating issues
    # url = "https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/issues"
    url = "https://api.github.com/repos/valeriec0/ai-exercise/issues"

    # Set the headers for the API request (including your personal access token)
    headers = {
        "Authorization": f"Bearer {os.environ.get('GITHUB_API_TOKEN')}"
    }

    # Set the data for the issue (title and body)
    data = {
        "title": title,
        "body": body
    }

    # Make the API request to create the issue
    response = requests.post(url, headers=headers, json=data)

    # Check the status code of the API response and print a message accordingly
    if response.status_code == 201:
        print("Github issue created successfully!")
    else:
        print("Error creating Github issue:", response.content)

@app.route('/', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data.get('prompt', '')
    title = f"New prompt: {prompt[:10]}"
    # https://platform.openai.com/docs/api-reference/chat/create
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    message = completion.choices[0].message.content
    body = f"Prompt: {prompt}\n\nGenerated text: {message}"
    create_github_issue(title, body)
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run()
