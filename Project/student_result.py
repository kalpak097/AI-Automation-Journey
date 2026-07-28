class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 35:
            return "D"
        else:
            return "Fail"


# Example Usage:
student1 = Student("Kalpak", 91)

print(f"Name: {student1.name}")
print(f"Marks: {student1.marks}")
print(f"Grade: {student1.grade()}")