### blueprint

class Car:
    def __init__(self,brand,model):
        self.brand = brand   # attribute
        self.model = model   # attribute

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")



### copies 

car1 = Car("BMW","X7")
car2 = Car("Audi","Q4")
car3 = Car("TATA","Nexon")

car1.drive()
car2.drive()
car3.drive()


class Driver:
    def __init__(self,name,rating,location):
        self.name = name
        self.rating = rating
        self.location = location
        
    def accept_ride(self):
        print(f"{self.name} has accepted the ride.")
        
driver1 = Driver("Tarun",5.0,"bangalore")
driver2 = Driver("Utej",5.0,"bangalore")

driver1.accept_ride()
driver2.accept_ride()