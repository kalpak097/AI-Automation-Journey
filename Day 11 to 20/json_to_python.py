import json

json_data = '''
{
    "name": "Kalpak",
    "age": 18,
    "course": "AI Automation"
}
'''

student = json.loads(json_data)

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])