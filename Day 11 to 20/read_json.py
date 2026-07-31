import json

try:
    with open("student.json", "r", encoding="utf-8") as file:
        student = json.load(file)

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("Skills:", student["skills"])

except FileNotFoundError:
    print("student.json was not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")