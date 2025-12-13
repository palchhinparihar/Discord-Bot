import discord, requests, json, os
from flask import Flask
from threading import Thread
from dotenv import load_dotenv


# Load .env file (optional for local development)
load_dotenv()


# ---------------------------
# Keep-alive web server
# ---------------------------
app = Flask('')


@app.route('/')
def home():
  return "Bot is alive!"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()


# ---------------------------
# Meme function
# ---------------------------
def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


# ---------------------------
# Discord bot
# ---------------------------
class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')


  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$meme'):
      meme1 = get_meme()
      text1 = "heellooooo! Here's a meme for you:"
      text2 = "Enjoy your meme! :)"
      await message.channel.send(f"{text1}\n{meme1}\n{text2}")


# ---------------------------
# Intents & run
# ---------------------------
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# Get token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)