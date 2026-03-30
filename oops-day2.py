


class Car:
    def __init__(self,brand ="BMW",model="X7"):
        self.brand = brand   # attribute
        self.model = model   # attribute
        print(f"{self.brand} {self.model} has been created.")

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")
        


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car()
car4 = Car("Ford", "Mustang")
car1.drive()