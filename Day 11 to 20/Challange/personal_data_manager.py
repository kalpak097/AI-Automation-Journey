import json
import os

FILENAME = "data.json"

def load_records():
    """Loads records from data.json, creating it if missing or corrupted."""
    if not os.path.exists(FILENAME):
        # Create an empty data.json file if it doesn't exist
        save_records([])
        return []

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read 'data.json' or file is corrupted. Re-initializing empty file.")
        save_records([])
        return []

def save_records(records):
    """Saves records back to data.json."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
    except IOError:
        print("Error: Failed to write data to file.")

def add_record(records):
    """Adds a new personal record with age validation."""
    name = input("Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    try:
        age = int(input("Age: "))
        if age < 0 or age > 120:
            print("Error: Age must be between 0 and 120.")
            return
    except ValueError:
        print("Error: Invalid age. Please enter a whole number.")
        return

    skill = input("Skill: ").strip()
    if not skill:
        print("Error: Skill cannot be empty.")
        return

    records.append({
        "name": name,
        "age": age,
        "skill": skill
    })
    
    save_records(records)
    print(f"Record for '{name}' added successfully!")

def view_records(records):
    """Displays all records stored in the file."""
    if not records:
        print("\nNo records found.")
        return

    print("\n--- ALL RECORDS ---")
    for idx, record in enumerate(records, 1):
        print(f"[{idx}] Name:  {record['name']}")
        print(f"    Age:   {record['age']}")
        print(f"    Skill: {record['skill']}")
        print("-" * 25)

def search_records(records):
    """Searches for records matching a name (case-insensitive)."""
    search_name = input("Enter name to search: ").strip().lower()
    if not search_name:
        print("Error: Search query cannot be empty.")
        return

    found = False
    for record in records:
        if record["name"].lower() == search_name:
            print("\n--- RECORD FOUND ---")
            print(f"Name:  {record['name']}")
            print(f"Age:   {record['age']}")
            print(f"Skill: {record['skill']}")
            found = True
            break

    if not found:
        print(f"No record found for '{search_name}'.")

def update_record(records):
    """Updates an existing person's age or skill."""
    search_name = input("Enter name to update: ").strip().lower()

    for record in records:
        if record["name"].lower() == search_name:
            print(f"\nUpdating record for {record['name']} (Press Enter to keep current value):")
            
            # Age update with validation
            age_input = input(f"New Age [{record['age']}]: ").strip()
            if age_input:
                try:
                    new_age = int(age_input)
                    if 0 <= new_age <= 120:
                        record["age"] = new_age
                    else:
                        print("Invalid age range (0-120). Keeping existing age.")
                except ValueError:
                    print("Invalid input. Keeping existing age.")

            # Skill update
            new_skill = input(f"New Skill [{record['skill']}]: ").strip()
            if new_skill:
                record["skill"] = new_skill

            save_records(records)
            print(f"Record for '{record['name']}' updated successfully!")
            return

    print(f"No record found for '{search_name}'.")

def delete_record(records):
    """Deletes a record by name."""
    search_name = input("Enter name to delete: ").strip().lower()

    for i, record in enumerate(records):
        if record["name"].lower() == search_name:
            removed = records.pop(i)
            save_records(records)
            print(f"Record for '{removed['name']}' deleted successfully.")
            return

    print(f"No record found for '{search_name}'.")

def main():
    """Main application control loop."""
    records = load_records()

    while True:
        print("\n===== PERSONAL DATA MANAGER =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Records")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            search_records(records)
        elif choice == "4":
            update_record(records)
        elif choice == "5":
            delete_record(records)
        elif choice == "6":
            print("Exiting Personal Data Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()