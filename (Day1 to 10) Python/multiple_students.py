class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name}: {self.marks}")

students = [
    Student("Kalpak", 95),
    Student("Rahul", 80),
    Student("Aisha", 91)
]

for student in students:
    student.display()