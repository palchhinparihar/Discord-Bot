from random import choice

messages = [
  'Hello, Hello! ✨',
  'Pong! 🏓 Diva Bot is alive.',
  'Hey there! Diva Bot here, ready to assist you! 💃',
  'Diva bot at your service! 🦄',
  'All systems operational! Pong from Diva Bot! 🤖',
  'Diva Bot checking in! Pong! 🏓',
  'What a beautiful day to be alive! 🌼',
]

def ping():
  return choice(messages)