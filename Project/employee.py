class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary}")

employee = Employee("Kalpak", 50000)

employee.display()