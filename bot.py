import discord, os, re
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

"""Discord Bot Client Class"""
class MyClient(discord.Client):
  # Event listener for when the bot is ready
  async def on_ready(self):
    print(f"Logged on as {self.user}!")

  # Event listener for messages
  async def on_message(self, message):
    # Ignore messages sent by the bot itself
    if message.author == self.user:
      return

    # Handle commands - $meme, $joke, $help, $ping, $pong, $diva
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
    elif re.match(r"^\$?(ping|pong|diva)$", message.content, re.IGNORECASE):
      await message.channel.send(ping())
    else:
      return

# Initialize and run the Discord client
intents = discord.Intents.default()
intents.message_content = True

# Create and run the client
client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))