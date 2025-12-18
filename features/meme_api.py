import requests
import json

"""Fetch a random meme from the meme API"""
def get_meme():
  response = requests.get('https://meme-api.com/gimme/me_irl')
  json_data = json.loads(response.text)
  return json_data['url']