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

def get_title_prompt(problem):
    return """I have a PROBLEM and want to generate a short title to file a Github issue for this problem

Please generate a title for the issue no more than 100 characters

PROBLEM:
""" + problem

def get_issue_prompt(problem):
    return """I have a PROBLEM, can you generate a github issue with the following ISSUE TEMPLATE:

ISSUE TEMPLATE:
## *Who* is the bug affecting?
<!-- Ex. All supervisors, Sally Supervisor, Level 1 CCs -->

## *What* is affected by this bug?
<!-- Ex. supervision, sending messages, texter profiles -->

## *When* does this occur?
<!-- Ex. After ending a conversation, every night at 3pm, when I sign off -->

## *Where* on the platform does it happen?
<!-- Ex. In the a Supervisor chat box, on the conversation profile page, on the two-factor screen -->


## *How* do we replicate the issue?
<!-- Please be specific as possible. Use dashes (-) or numbers (1.) to create a list of steps -->


## Expected behavior (i.e. solution)
<!-- What should have happened? -->


## Other Comments

PROBLEM:
    """ + problem

@app.route('/', methods=['POST'])
def generate_text():
    data = request.get_json()
    problem = data.get('problem', '')
    title_prompt = get_title_prompt(problem)
    issue_prompt = get_issue_prompt(problem)
    # https://platform.openai.com/docs/api-reference/chat/create
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": title_prompt}
        ],
    )
    title = completion.choices[0].message.content
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": issue_prompt}
        ],
    )
    body = completion.choices[0].message.content
    body_with_problem = f"""{body}
<br/><br/>
## Logs

```
{problem}
```
"""
    create_github_issue(title, body_with_problem)
    return jsonify({'title': title, 'body': body_with_problem})

if __name__ == '__main__':
    app.run()
