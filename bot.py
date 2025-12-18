import discord, os
from dotenv import load_dotenv

from main import keep_alive
from features.meme_api import get_meme
from features.random_joke_api import get_joke
from utils.help_cmd_api import help_text
from utils.ping import ping

# Load environment variables
load_dotenv()

# Start Flask server
keep_alive()

# Create a subclass of Client
class MyClient(discord.Client):
  async def on_ready(self):
    print(f"Logged on as {self.user}!")

  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith("$meme"):
      embed = discord.Embed(
        description="Here's a meme for you 😶‍🌫️\nEnjoy your meme!"
      )
      embed.set_image(url=get_meme())
      await message.channel.send(embed=embed)
    elif message.content.startswith("$joke"):
      title = "Wanna hear a joke? There you go 👻"
      embed = discord.Embed(
        description=get_joke()
      )
      await message.channel.send(title, embed=embed)
    elif message.content.startswith("$help"):
      await message.channel.send(help_text())
    elif message.content.startswith("$ping"):
      await message.channel.send(ping())
    else:
      return

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))
