from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
  return "Girl what are you doing here? Go check out the bot. It is alive! :)"

# Function to run the Flask app
def run():
  port = int(os.environ.get("PORT", 10000))
  app.run(host="0.0.0.0", port=port)

# Function to keep the server alive
def keep_alive():
  Thread(target=run).start()