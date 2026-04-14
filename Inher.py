"""
## Parent class

class Animal :
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes a sound")
        
    
    
# Child class 

class Dog(Animal) :
    pass
        
        

class Cat(Animal) :
    pass
        
        
        
dog = Dog("max")

print(dog.speak())

cat = Cat("melow")


print(cat.speak())
"""

class User :
    def __init__(self,name):
        self.name = name
    
    def login(self):
        print(f"{self.name} logged in")
        

# Drive
class Drive(User):
    
    def navigate(self):
        pass

# Rider
class Rider(User):
    
    def request_ride(self):
        print(f"{self.name} is requesting a ride.")
        
        
class AndroidNav:
    def androidnav(self):
        print("this is android navigation")

class IosNav:
    print("this is android navigation")
        
class Navigation(Drive,AndroidNav,IosNav):
    
    
    def navigation(Self):
        pass
        
        
        
Driver1 = Drive("tarun")
Rider1  = Rider("teja")


Driver1.login()


Rider1.login()

Rider1.request_ride()

Driver1.navigate()



        