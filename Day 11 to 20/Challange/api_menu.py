import requests

def get_random_joke():
    """Fetches a random setup and punchline joke."""
    url = "https://official-joke-api.appspot.com/random_joke"
    print("\nFetching joke...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("\n--- Random Joke ---")
        print(f"Setup:     {data.get('setup')}")
        print(f"Punchline: {data.get('punchline')}")

    except requests.RequestException as e:
        print(f"Could not retrieve joke: {e}")
    except (KeyError, ValueError):
        print("Received invalid joke data from the server.")

def get_country_info():
    """Fetches basic details about a country by name."""
    country = input("\nEnter country name: ").strip()
    if not country:
        print("Country name cannot be empty.")
        return

    url = f"https://restcountries.com/v3.1/name/{country}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()[0]
        name = data.get("name", {}).get("common", "N/A")
        capital = data.get("capital", ["N/A"])[0]
        region = data.get("region", "N/A")
        population = f"{data.get('population', 0):,}"

        print("\n--- Country Information ---")
        print(f"Name:       {name}")
        print(f"Capital:    {capital}")
        print(f"Region:     {region}")
        print(f"Population: {population}")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("Country not found. Please check the spelling.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.RequestException:
        print("Could not retrieve country information. Check your internet connection.")
    except (KeyError, IndexError, ValueError):
        print("Unexpected data format received from the API.")

def get_random_quote():
    """Fetches a random quote using ZenQuotes API."""
    url = "https://zenquotes.io/api/random"
    print("\nFetching quote...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()[0]

        print("\n--- Daily Quote ---")
        print(f'"{data.get("q")}"')
        print(f"- {data.get("a")}")

    except requests.RequestException as e:
        print(f"Could not retrieve quote: {e}")
    except (KeyError, IndexError, ValueError):
        print("Received invalid quote data from the server.")

def main_menu():
    """Main application loop."""
    while True:
        print("\n===== API TOOL =====")
        print("1. Get Random Joke")
        print("2. Get Country Information")
        print("3. Get Random Quote")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            get_random_joke()
        elif choice == "2":
            get_country_info()
        elif choice == "3":
            get_random_quote()
        elif choice == "4":
            print("\nThank you for using API Tool. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()