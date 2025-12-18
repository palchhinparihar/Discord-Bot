# Discord-Bot 

> A cozy, modular Discord bot to brighten up your server with memes, jokes, and friendly vibes.

---

## ✨ Features

- **Meme Command**: `$meme` - Get a random meme from the internet, delivered with a warm touch.
- **Joke Command**: `$joke` - Enjoy a random joke.
- **Ping, Pong, Diva**: `$ping`, `$pong`, `$diva` - Check if the bot is alive with a playful status message.
- **Help Command**: `$help` - See all the cozy commands you can use.
- **Custom Help**: Friendly, easy-to-read help text.
- **Always Awake**: Stays online with a tiny Flask web server (great for Replit, Render, etc).
- **Modular Structure**: All features and utilities are neatly organized for easy editing.

---

## 🗂️ File Structure

```
bot.py                # Discord bot logic & command handling
main.py               # Flask server to keep bot alive
requirements.txt      # Python dependencies
features/
  meme_api.py         # Fetches memes from meme-api.com
  random_joke_api.py  # Fetches jokes from Official Joke API
utils/
  help_cmd_api.py     # Help command text
  ping.py             # Ping/pong/diva responses
```

---

## 🚀 Getting Started

1. **Clone this repo**
	```
	git clone https://github.com/palchhinparihar/Discord-Bot.git
	```
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Add your Discord token**
- Create a `.env` file:
     ```
     DISCORD_TOKEN=your_token_here
     ```
4. **Run the bot**
   ```
   python bot.py
   ```

---

## 💬 Commands

| Command      | What it does                        |
|--------------|-------------------------------------|
| `$meme`      | Sends a random meme                 |
| `$joke`      | Replies with a random joke          |
| `$ping`, `$pong`, `$diva`   | Bot replies with a status message   |
| `$help`      | Lists all available commands        |

---

## 🌱 Extend & Enjoy

Feel free to add your own features, tweak responses, or just enjoy the cozy vibes! The code is organized for easy editing and extension.

---

*Thanks to [Codédex](https://github.com/codedex-io) for the inspiration.*

Have any question? Email me on [this](palchhinparihar@gmail.com).

**Made by [Palchhin](https://palchhin.me)~**