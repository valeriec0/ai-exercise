# this is the script to test the web server
import requests
import json

url = 'http://127.0.0.1:5000/'
prompt = 'Hello, GPT-3!'
data = {'prompt': prompt}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.text)
else:
    print('Error:', response.status_code, response.text)
