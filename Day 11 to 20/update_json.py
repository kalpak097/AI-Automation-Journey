import json

try:
    with open("student.json", "r", encoding="utf-8") as file:
        student = json.load(file)

    student["age"] = 19
    student["skills"].append("JSON")

    with open("student.json", "w", encoding="utf-8") as file:
        json.dump(student, file, indent=4)

    print("Student information updated!")

except FileNotFoundError:
    print("student.json was not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")