class Animal :
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        print(f"{self.name} makes a sound")
        
    
    
# Child class 

class Dog(Animal) :
    def speak(self):
        print(f"{self.name} is barking")
        
        

class Cat(Animal) :
    def speak(self):
        print(f"{self.name} is mewow")
        
        
        
dog = Dog("max")

#dog.speak())

cat = Cat("melow")


#cat.speak())


lis = [1,2,3,4,5,6,7,8,9]

st = "tarun"


print(len(lis))
print(len(st))

print("string")
print(123213)
print(['list','elements'])

