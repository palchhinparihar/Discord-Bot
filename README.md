
# Discord-Bot

This is a feature-rich Discord bot that responds to various commands, sends memes and jokes, and provides helpful utilities.

## Features
- Responds to the following commands:
	- `$meme` — Sends a random meme from the internet.
	- `$joke` — Replies with a random joke (using JokeAPI).
	- `$ping` — Checks if the bot is alive with a fun message.
	- `$help` — Lists all available commands.
- Custom help command with all available features.
- Keeps itself alive using a small Flask web server (for hosting on platforms like Replit or Render).
- Modular code structure with separate files for features and utilities.

## File Structure

```
bot.py                # Main Discord bot logic
main.py               # Flask server to keep bot alive
requirements.txt      # Python dependencies
features/
	meme_api.py         # Fetches memes from meme-api.com
	random_joke_api.py  # Fetches jokes using JokeAPI
utils/
	help_cmd_api.py     # Help command text
	ping.py             # Ping command responses
```

## Usage
1. Clone this repository.
2. Install dependencies:
	```
	pip install -r requirements.txt
	```
3. Create a `.env` file with your Discord bot token:
	```
	DISCORD_TOKEN=your_token_here
	```
4. Run the bot:
	```
	python bot.py
	```

## Commands
- `$meme` — The bot replies with a random meme and custom text.
- `$joke` — The bot replies with a random joke.
- `$ping` — The bot replies with a random status message.
- `$help` — The bot lists all available commands.

---
Feel free to modify or extend the bot!

Thanks to [Codedex](https://github.com/codedex-io) for the tutorial. :)
