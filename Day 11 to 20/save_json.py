import json

student = {
    "name": "Kalpak",
    "age": 18,
    "course": "AI Automation",
    "skills": ["Python", "APIs", "GitHub"]
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Student data saved!")