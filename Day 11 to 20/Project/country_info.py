import requests

country = input("Enter country name: ")
url = f"https://restcountries.com/v3.1/name/{country}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    country_data = data[0]

    print("\n--- Country Information ---")
    print("Name:", country_data["name"]["common"])
    
    # Capital is a list, safely fetch the first element if available
    capital = country_data.get("capital", ["N/A"])[0]
    print("Capital:", capital)
    
    print("Region:", country_data.get("region", "N/A"))
    print("Population:", f"{country_data.get('population', 0):,}")

except requests.exceptions.HTTPError as http_err:
    if response.status_code == 404:
        print("Country not found. Please check the spelling.")
    else:
        print(f"HTTP error occurred: {http_err}")
except requests.RequestException:
    print("Could not retrieve country information. Please check your internet connection.")
except (KeyError, IndexError):
    print("Unexpected data structure received from the API.")