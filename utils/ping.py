from random import choice

messages = [
  'pong! 🏓 Diva Bot is alive.',
  'hey there! Diva Bot here, ready to assist you! 🏓',
  'Diva Bot at your service! Pong! 🏓',
  'all systems operational! Pong from Diva Bot! 🏓',
  'Diva Bot checking in! Pong! 🏓'
]

def ping():
  return choice(messages)