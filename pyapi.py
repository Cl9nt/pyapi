# import python requests library

import requests 

import json

# connect to the api

response_API = requests.get("https://gmail.googleapis.com/$discovery/rest?version=v1")

# response code

print(response_API.status_code)

data = response_API.text

parse_json = json.loads(data)

info = parse_json['description']

print(" Info about API : \n ", info)

key = parse_json['parameters']['key']['description']

print("\n Description about the key : \n", key)