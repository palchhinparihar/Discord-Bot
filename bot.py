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

# ---------------------------
# Run server
# ---------------------------
def run():
  port = int(os.environ.get("PORT", 10000))
  app.run(host="0.0.0.0", port=port)


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
      text1 = "heellooooo! here's a meme for you:"
      text2 = "enjoy your meme! :)"

      embed = discord.Embed(description=f"{text1}\n{text2}")
      embed.set_image(url=meme1)
      await message.channel.send(embed=embed)


# ---------------------------
# Intents & run
# ---------------------------
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# Get token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)