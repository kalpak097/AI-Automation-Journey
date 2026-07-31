import json
import os
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
FILENAME = "users.json"

def fetch_and_save_users():
    """Fetches user data from the API, extracts key fields, and saves to JSON."""
    print("Fetching users from API...")
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        raw_users = response.json()

        # Extract and format target fields
        formatted_users = []
        for user in raw_users:
            formatted_users.append({
                "name": user.get("name", "N/A"),
                "email": user.get("email", "N/A"),
                "city": user.get("address", {}).get("city", "N/A")
            })

        # Save extracted list to users.json
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(formatted_users, file, indent=4)

        print(f"Successfully saved {len(formatted_users)} users to '{FILENAME}'.")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch users from API: {e}")
    except IOError as e:
        print(f"Failed to write data to file: {e}")

def load_and_display_users():
    """Reads users from users.json and displays them."""
    if not os.path.exists(FILENAME):
        print(f"Error: File '{FILENAME}' does not exist.")
        return

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            users = json.load(file)

        print("\n=== SAVED USERS DATABASE ===")
        for idx, user in enumerate(users, 1):
            print(f"[{idx}] Name:  {user['name']}")
            print(f"    Email: {user['email']}")
            print(f"    City:  {user['city']}")
            print("-" * 30)

    except json.JSONDecodeError:
        print("Error: Could not decode JSON data from file.")
    except IOError as e:
        print(f"Error reading file: {e}")

def main():
    # Step 1: Fetch from API and save to JSON
    fetch_and_save_users()

    # Step 2: Read back from JSON and display
    load_and_display_users()

if __name__ == "__main__":
    main()