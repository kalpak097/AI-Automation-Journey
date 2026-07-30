import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    users = response.json()

    # Open the output file in write mode
    with open("diary.txt", "w", encoding="utf-8") as file:
        file.write("--- USER DIRECTORY ---\n\n")
        
        for user in users:
            name = user.get("name", "N/A")
            email = user.get("email", "N/A")
            # City is nested inside the address object
            city = user.get("address", {}).get("city", "N/A")

            file.write(f"Name:  {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"City:  {city}\n")
            file.write("-" * 30 + "\n")

    print("Users successfully saved!")

except requests.exceptions.RequestException as e:
    print(f"Failed to fetch users from API: {e}")
except IOError as e:
    print(f"Failed to write to diary.txt: {e}")