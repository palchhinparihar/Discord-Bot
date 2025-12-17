# Discord-Bot

This is a simple Discord bot that responds to commands and sends memes.

## Features
- Responds to the `$meme` command by sending a random meme, each with custom messages.
- Keeps itself alive using a small Flask web server (for hosting on platforms like Replit or Render).

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
- `$meme` — The bot replies with a meme and custom texts.
<img width="575" height="631" alt="image" src="https://github.com/user-attachments/assets/08487e25-a81e-4ab1-ac95-c6562d335d66" />

---
Feel free to modify or extend the bot!
Thanks to [Codedex](https://github.com/codedex-io) for the tutorial. :)
