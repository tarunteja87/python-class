

class Car:
    def start(self):
        print("car is started")
        
    def drive(self):
        print("Car is moving")
        
        
my_car = Car()


#my_car.start()
#my_car.drive()


#simple abstraction 

from abc import ABC, abstractmethod

# area of circle - pi * r ** 2
# area of rectangle 
# area of square    -  
# area of triangle   - 0.5 * base * height 



## parent class
class Shape(ABC):
    
    
    # area is declared but not implemented
    # hi developers i want everyone to use this area for all the shapes youa re creating ( graphis - needs area all the time - )
    @abstractmethod
    def area(self):
        pass
    
    
class Circle(Shape):
    
    def area(self):
        return "area"
    
    def summary(Self):
        print("this is the summary")


circle1  = Circle()

circle1.summary()
    

