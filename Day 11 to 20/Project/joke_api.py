import requests

url = "https://official-joke-api.appspot.com/random_joke"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    joke = response.json()

    print("Type:", joke["type"])
    print("Setup:", joke["setup"])
    print("Punchline:", joke["punchline"])

except requests.RequestException as error:
    print("Error:", error)