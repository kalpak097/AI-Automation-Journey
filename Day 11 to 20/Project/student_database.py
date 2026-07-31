import json
import os

FILENAME = "students.json"

def load_students():
    """Loads student records from the JSON file."""
    if not os.path.exists(FILENAME):
        return []
    
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read students.json or file is corrupted. Starting with an empty database.")
        return []

def save_students(students):
    """Saves the student records back to the JSON file."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
    except IOError:
        print("Error: Failed to write data to file.")

def add_student(students):
    """Adds a new student to the list."""
    name = input("Name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return

    try:
        marks = float(input("Marks: "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Invalid input for marks. Please enter a number.")
        return

    students.append({"name": name, "marks": marks})
    save_students(students)
    print(f"Student '{name}' added successfully!")

def view_students(students):
    """Displays all students stored in the database."""
    if not students:
        print("\nNo students found in the database.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print("-" * 20)

def search_student(students):
    """Searches for a student by name (case-insensitive)."""
    search_name = input("Enter student name: ").strip().lower()
    
    found = False
    for student in students:
        if student["name"].lower() == search_name:
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            found = True
            break
            
    if not found:
        print(f"No student found with the name '{search_name}'.")

def update_marks(students):
    """Updates the marks of an existing student."""
    search_name = input("Enter student name to update: ").strip().lower()

    for student in students:
        if student["name"].lower() == search_name:
            try:
                new_marks = float(input(f"Enter new marks for {student['name']}: "))
                if not 0 <= new_marks <= 100:
                    print("Marks must be between 0 and 100.")
                    return
                student["marks"] = new_marks
                save_students(students)
                print(f"Marks updated successfully for {student['name']}!")
                return
            except ValueError:
                print("Error: Invalid input for marks. Update canceled.")
                return

    print(f"No student found with the name '{search_name}'.")

def delete_student(students):
    """Deletes a student record by name."""
    search_name = input("Enter student name to delete: ").strip().lower()

    for i, student in enumerate(students):
        if student["name"].lower() == search_name:
            removed_student = students.pop(i)
            save_students(students)
            print(f"Student '{removed_student['name']}' has been deleted successfully.")
            return

    print(f"No student found with the name '{search_name}'.")

def main():
    """Main application loop."""
    students = load_students()

    while True:
        print("\n===== STUDENT DATABASE =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_marks(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting Student Database. Goodbye!")
            break
        else:
            print("Invalid option! Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()