# Discord-Bot

This is a simple Discord bot that responds to commands and sends memes.

## Features
- Responds to the `$meme` command by sending two random memes, each with a custom message.
- Keeps itself alive using a small Flask web server (for hosting on platforms like Replit).

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
- `$meme` — The bot replies with two memes and custom texts.

---
Feel free to modify or extend the bot!