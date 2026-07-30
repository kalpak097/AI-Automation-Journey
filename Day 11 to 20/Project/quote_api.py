import requests

url = "https://api.quotable.io/random"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    print("\nQuote:")
    print(f'"{data["content"]}"')

    print("\nAuthor:")
    print(data["author"])

except requests.exceptions.RequestException as e:
    print("Could not retrieve quote:", e)

except KeyError:
    print("Unexpected JSON response structure.")