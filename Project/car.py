class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        print(f"{self.brand} {self.model}")

car1 = Car("Toyota", "Fortuner")
car2 = Car("Tesla", "Model 3")

car1.show()
car2.show()