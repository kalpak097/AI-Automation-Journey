student = {}

student["name"] = input("Name: ")
student["age"] = int(input("Age: "))
student["course"] = input("Course: ")

print("\nStudent Details")

for key, value in student.items():
    print(f"{key}: {value}")