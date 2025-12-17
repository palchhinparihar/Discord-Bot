from jokeapi import Jokes
import traceback

async def get_joke():
  try:
    j = await Jokes()
    joke = await j.get_joke()

    if joke["type"] == "single":
      return joke["joke"]
    else:
      return f"{joke['setup']}\n{joke['delivery']}"
  except Exception as e:
    print("Error in get_joke():", e)
    traceback.print_exc()
    return "Sorry, I couldn't fetch a joke right now. 😢"
