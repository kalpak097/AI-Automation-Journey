name = input("Student Name: ")
marks = input("Marks: ")

with open("students.txt", "a") as file:
    file.write(f"{name} - {marks}\n")

print("Student record saved.")