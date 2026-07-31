import json

student = {
    "name": "Kalpak",
    "age": 18,
    "course": "AI Automation",
    "skills": ["Python", "Git", "APIs"]
}

json_data = json.dumps(student, indent=4)

print(json_data)