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
        description="heellooooo! here's a meme for you 😄\nenjoy your meme!"
      )
      embed.set_image(url=get_meme())
      await message.channel.send(embed=embed)
    elif message.content.startswith("$joke"):
      joke = await get_joke()
      title = "wanna hear a joke? there you go 😂"
      embed = discord.Embed(
        description=joke
      )
      await message.channel.send(title, embed=embed)
    elif message.content.startswith("$help"):
      await message.channel.send(help_text())
    else:
      await message.channel.send(ping())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))
