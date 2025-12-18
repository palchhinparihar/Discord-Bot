import requests
import json

"""Fetch a random joke from the joke API"""
def get_joke():
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  json_data = json.loads(response.text)
  return json_data['setup'] + "\n" + json_data['punchline']