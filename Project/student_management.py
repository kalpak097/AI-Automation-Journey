students = {}

# Input 5 students and their marks
for i in range(1, 6):
    name = input(f"Enter name for student {i}: ")
    mark = float(input(f"Enter mark for {name}: "))
    students[name] = mark

print("\n--- Student Results ---")
for name, mark in students.items():
    status = "Pass" if mark >= 35 else "Fail"
    print(f"Name: {name} | Marks: {mark} | Status: {status}")

# Find the topper
topper_name = max(students, key=students.get)
topper_marks = students[topper_name]

print("\n--- Topper ---")
print(f"Topper: {topper_name} with {topper_marks} marks")