# Python server + test script

A Python endpoint that create Github issues based on reported problems. A test script to hit the server running locally to create Github issues based on problem logs provided.

## Installation

make sure you are in the `py` directory
`pip3 install -r requirements.txt`

## Usage

Running the server
1. Make a copy of `.env.example` and name it `.env`.
1. Replace the environment variable values following the instructions for each variable
1. `cd py` to go into the  `py` folder
1. start the server with `python3 app.py`

Generating a Github Issue
1. replace the `problem` variable in `test.py` with lines of logs. One possibility is from the [loghub repository](https://github.com/logpai/loghub)
1. run test.py
1. see in your configured Github repository a new issue filed based on the logs provided.

## Acknowledgments

* [Openai Chat GPT API](https://platform.openai.com/docs/api-reference/chat/create)
* Chat GPT