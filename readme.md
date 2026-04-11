# Python Class

Python + OOP

Django/Flask

REST APIs

SQL (PostgreSQL/MySQL)

Frontend (React)

Git

Basic AWS

## What is python
- Python is a programming language , which helps to communicate with th hardware components of the computer.
## why Python
- Its simple to undertand (Readibility)
- High level language - 
- Simple to learn 
- high level programming language
- Interpreted language.
- Dynamically Types.



## Levels of languages
- High (python , its like human langue)
    - No nned to worry about  memory 
    - pointer
    - Hardware details
- low (machine level language - binary languagge (0,1))
- Medium (c is good exam - having set of rules and , you can directly communicate with hardware , manipulatling the memory object , int , float )

## General- puropse of python
- Web sites
- AI/ ML - chat bots , agents, 
- Data science - 
- Automation
- Testing 
- Game Development . ( C++)

## Compiled vs intrepted
- C -> complie -> the run  - after compilation we will get to know the error - if the error is at the end of the code - this will fails 
- If there is error at end - the whole code will execute and stops at the error line.
    - Python runs line by line using an intrepreter.

# What the market demand for python developers and whats the different pathways
- High demand 
- Django , Fastapi, Some devops concept



# Basics of python
### Variables
- varable = a container that stores data


### Datatypes :
- int
- float 
- str
- bool 

Exmaple :
- product name : string : str
- price : float
-  qunatity : int
- payment status : True / False  - boolean


```python
product_name = "laptop"
price  =  23.75 # float
qunatity = 2 #int
is_paid = True # bool

print("Product:" , product_name)
print("price ", price )
print("qunatity ", qunatity )
print("is_paid" ,is_paid)

total_amount =  price*quantity

print("total amount :",total_amount)
```

#### Task

```
name = "Your Name"
age = 22
height = 5.8
is_student = True

print(name, age, height, is_student)
```

```https://www.python.org/downloads/```

## Taking inputs and Type conversion
### What is input ?
- `input()` allows the program to take data from the users.
- by default input is always stored as a **string**

```python

age = input("Enter the age : ")
print(type(age)) #class 'str'

# for year - 365
# age * 365
```

### Type Conversion


| **Function** | **Converts to** |
| -------------| ----------|
| int() | integer|
| float() | decimal|
| str() | string |
| bool() | boolean |

### Operators

> Operator = symbol that perform an action

```
5 + 3
```

`+` is the operator  
`5` and `3` are operands

|Operator	|Meaning	| Example|
| ----- | ---- | ---- |
|+	|Addition	|a + b
|- |	Subtraction |	a - b
|*	|Multiplication	|a * b
|/	|Division	| a / b
|//	|Floor division |	a // b
|% | 	Modulus	|a % b
|**	|Power	|a ** b


```python
price = 499
quantity = 3

total = price * quantity
discount = total * 0.10
final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
```

## Comparison Operators
| Operator | Meaning          |
| -------- | ---------------- |
| ==       | equal            |
| !=       | not equal        |
| >        | greater than     |
| <        | less than        |
| >=       | greater or equal |
| <=       | less or equal    |


``` python
entered_pin = 1234
actual_pin = 1234

print("PIN Match:", entered_pin == actual_pin)
print("PIN Wrong:", entered_pin != actual_pin)

```

## Logical operators
| Operator | Meaning           |
| -------- | ----------------- |
| and      | both must be true |
| or       | at least one true |
| not      | reverses result   |


### Day 3 Task :
- Problem: Restaurant Bill Generator

```
**Take from user:**
customer name
food price
quantity
tax = 5%

**Calculate:**
total
tax amount
final bill
```


# Day 4

## Conditional Statements (if - else)

- Conditioinal statements allows python to execute code based on a condition.

```python
 
if <condition>:
    # do this for me (code runs if condition is true)
else :
    # code runs  - if  condiotion false

```

```python

# if balance >= withdrawl amount -> allow the operation
# else : tells  notify the user regarding the issue.

if connection success:
    do some progress - the operation (deposit , withdraw, balance check etc.)
else :
    prit("atm out of service")

```

> https://github.com/thonny/thonny/releases/tag/v4.1.7

### Task on if - else 
>we have to check the eligibility to vote  for the user
> - user  should have age at least 18 or above 
> - we hav to take the input from the user .
> - take user name from the user an dnotify the user with their name 
>- name : tarun - and age is 18 means you have print "tarun you are eligible to vote" esle  "tarun your are not eligible to vote" 

#### Solution
```python

#we have to take the input from the user .
age = int(input("Enter your age : "))

#user should have age at least 18 or above
#PEP 8 - standards for python programming

if age >= 18:
    print("User is eligible to vote")
else :
    print("user is not eligible to vote")

```

### if -elif - else  (Multiple conditions)
- used when there are many choices

``` python
## this is Syntax
if condition1:
    pass
elif  condition2:
    pass
elif condtion3:
    pass
else:
    pass

```

#### Coding Example:
>1. take marks from the user
>2. if marks is greater than or equal to 90 -> print Grade A
>3. if marks is greater than or equal to 75 -> print Grade B
>4. if marks is greater than or equal to 50 -> print Grade c

```python 
marks = int(input("Enter your marks :"))

if marks >= 90 :
    print("Grade :A")
elif marks >= 75 :
    print("Grade :B")
elif marks >=50 :
    print("Grade :C")
else :
    print("Fail")

```

#### task : 
> take number the user and print odd even number

> take two number and print nthe largest number 

## TOPICS 5 LOOPS
- Loops allows  us to `repeat a block of code multiple times`
Intead of writing the same code again and again , we use loops

### Types of loops in python:
1. for loop
2. while loop


```python 
for <variable> in  range(number):
    #code
```

### For loop inside for loop (nested for loop)




- our aim is to print 5 numbers from 0



### Lists 

- list is a container **that stores multiple values in one varaible**
Eg: A**Shopping cart** stores many items.

``` python

fruits = ["Apple","Banana","Mango"]

print(fruits)
## each item seperated by commas
```

## accessing Items

Each item ha  s position (index)

``` python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

```

### Adding Items

``` python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

append() → adds item to list.

```python
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print(cart)

```


### tasks
- Create a list of 3 favorite movies and print them.
- Create a list of 5 numbers and print the first number.
- Create an empty list and add 3 fruits using append().

## Strings

- Text inside **quotes** is called a string.
> "hello"
> 'hello'

### String Index

```python
name = "Python"

print(name) # Python
print(name[0]) # P
print(name[1]) # y
print(name[-1])
```
### String Slicing 

```python
text = "python"
print(text[0:3])  #Pyt
```

### String Funcrtions


```python
text = "python"
print(text.upper())  # PYTHON
```


```python
text = "PYTHON"
print(text.lower())  # python
```


### length of string

```python
text = "PYTHON"
print(len(text))  # 6
```

#### Example:
```python
usename = input("Enter user name : ")

if username == "tarun":
    print("access Granted ")
else :
    print("Access denied")

```
## While Loop 
- (for loop will excute the task based on the range :)
- A **While loop repeates code** while a condition is True

```python
while condition:
    #code to execute
```

### Simple Example
- print numbers from 1 to 5
```python
password = input(" Enter the password : ")

my_password = "Tarun"

while password !=  my_password:
    password = input(" your password is incorrect please  Enter the correct password : ")
    
print(" user verification successful")


```

```python
password = input(" Enter the password : ")

my_password = "Tarun"
count = 0

while password !=  my_password and count < 2:
    password = input(" your password is incorrect please  Enter the correct password : ")
    count = count + 1

if count >=2 :
    print("please try after some time")
else:
    print(" user verification successful")
```
```python
#print( 1 to 5 using while loop)
number = 1

while number <=5 :
    #code
    print(number)
    number+=1   # number = number +1
    
    
    
### 5 4 3 2 1
```
## Do -while concept
- Do while loop executes the code at least once before checking the condition

```python
# Do while 
Run Code
|
Check condition
|
Repeat
```

```
Check condition
|if above condition is true
Run the code 
|
Repeat
```

```
do 
{
    print("hello")
} while(condition)
```

```python
while True :
    num = int(input("enter a number greater than 10 : "))

    if num >10:
        break

# loop runs first
# condition checked later
# break stops the loop - 
```
---------------------------------
|Feature | While loop |  do-while|
--------|-------------|------------
|Condition check | before loop | After loop|
|Runs at least once| no |Yes|

## Dictionaries in Python
- A dictonary stores data in key-value pairs.

```Python
Name -> tarun
Age  -> 25
City -> Banglore
```

```python
student = {"name":"tarun", "age":25,"city":"Banglore","phone_number":995122222} :XX
```

```python

student = {
    "name":"tarun",
    "age":25,
    "city" : "Banglore",
    "phone _number" : 99232323223
    }
```

```
{ }
key - > value 

```

```python
print(student)

#o/p : {'name':'tarun', 'age':25,'city':'Banglore','phone_number':995122222} 
```

### How to access elements in dictonary

```python
print(dictonary_name['key'])
```

```python

student = {
    "name":"tarun",
    "age":25,
    "city" : "Banglore",
    "phone _number" : 99232323223
    }

print(student['age'])


for key in student:
    print("key : "+key)
    print("value : " + str(student[key]))
    print( "_"*10)
```

## How to change values for a key in the dictonary

```python

student = {
    "name":"tarun",
    "age":25,
    "city" : "Banglore",
    "phone _number" : 99232323223
    }

print(student)

student["name"] = "Teja"

print(student)

student["age"] = 23
print(student)
```

### How to add elements in the dictonary
```python

student = {
    "name":"tarun",
    "age":25,
    "city" : "Banglore",
    "phone _number" : 99232323223
    }

print(student)

student["name"] = "Teja"

print(student)

student["age"] = 23
print(student)

### add data to the dictonary
student["address"] = "Andhra"

print(student)


### Add list to the key
student["address"] = ['Vizag','Andhra',533333]
```
### how to delete data in the dictonary

```python

student = {
    "name":"tarun",
    "age":25,
    "city" : "Banglore",
    "phone _number" : 99232323223
    }
student.pop("address")

print(student)

```

## Nested loops


```python
list_students = [
    ['tarun',20,'ECE'],
    ['balakrishna',21,'cse'],
    ['indresh',21,'EEE'],
    ['Karthik',22,'AI']
]


for student in list_students :
    for item in student:
        print(item)
    print('_'*10)

```
```
*
**
***
****
*****
```

```
****
****
****
****
```


```
*
**
***
****
*****
****
***
**
*
```

```
1
12
1234
12345
123456
```

```python
"""
1
12
123
1234
12345
123456
"""


#print('1')
#print('1 2')
#print('1 2 3 ')
#print('1 2 3 4')

number = 4

for i in range(1,number + 1):           
    for j in range(1,i + 1):			
        print(j ,end = " ")
    print("")
     
```

```
111
222
333
```

## Functions 
- A function is a block of code that performs a specific task.
- we call function whenever we need it.

### Basic Syntax of a function

```python
def greet():
    print("Hello Students")
```

```python
## example for naming 
def add():
    return  a+b

```

| Keyword | Meaning|
|---------|--------|
|def | defines a function|
|greet | function name|
|( )| parameters|

> The function runs only when we call it

#### Function with parameters

```python
#machine  needs to greet with the user name 
# machine to prepare a coffee based on the options the user choose

# cold , hot , mild , hard , strong , light 


def coffee_machine(coffee_type,quantity):
    instruction = coffee_type
    print(quantity + " " + coffee_type + " Coffeee is ready ")
    

coffee_machine("cold","200ml")

```
### Functions with Return Value

- Function can return results


```python 
def coffee_machine(coffee_type,quantity):
    instruction = coffee_type
    print(quantity + " " + coffee_type + " Coffeee is ready ")
    return "coffee"

#cup = coffee_machine("cold","200ml")


#print(cup)

#print("sugar " + cup)


def add(num1,num2):
    result = num1 + num2
    return result


res = add(1,1)
print(res) #2


res2 = add(res,1)
print(res2) #3
```

- `return` sends the resukt back

## File Handiling in Python

- File handing allows python program to create , read , write , and update files.

- Example : invoice , logs , reports , configrations


___

- we use    `open()` function function .


```python

file_content = open('test.txt','r')

```

| Mode | Meanings|
|---|-----|
|r| read file|
|w| write file|
|a| append data
|x | create new file|
____

### read
```python
###########  READ ##############

file = open("test.txt", "r")  # open the file in read mode.

content = file.read()  # read the content of the file.

print(content)  # print the content of the file.

file.close()  # This is the important step when you use open function
```

### Write
```python
################ Write ###################

file = open("test.txt", "w")


file.write(" hello students this is writing from the code")


file.close()
```

### Append

```python
###### Append #######

file = open("test.txt", "a")

file.write("\nthis is appended text ")

file.close()
```

### Create

```python
file = open("text.txt","w")

file.write("hello this is the file created using open function in python")

file.close()
```



#### Task
- take inputs from user : Name , age , height , weight  and calculate BMI 
- Generate a report (report.txt ) file should contains - name , age , height , weight and BMI


## Exception Handling\ what is exception handling?
Exception Handling is used to handle errors without crashing the program.


```python
number = int(input("Enter the number : "))

print(10/number)

print("this is some more program to run.")
```
### Specific Exceptions :

```python

try :
    print(10/number)
except ZeroDivisionError:
    print("Cannot divide by zero")
except :
    print("this is unknown error")

print("this is some more program to run.")
```
### Else and finally

```python
number = int(input("Enter the number : "))

try :
    print(10/number)
    
except ZeroDivisionError:
    print("Cannot divide by zero")
except :
    print("this is unknown error")

else : 
    print("there are no errors found")
    
finally:
    print("finally always works")
    
    
print("this is some more program to run.")

```
## OOPS
Oops is a way of writing code using `objects` and `classes`.

example :
 Application form(template) - 

 1. you download the application form and you have fill. (copy)
 2. a

- `class` is like a blueprint
- `objects` is the copy of the blueprint( with or with out modifications)

### Class and object
- A `class` is a blueprint for creating an object. an `object` is an isntance of class - a real world entity behaviour (car can drive ) attributes(colour :white)

- A `class` defines what kind of data and functions(methods) the object will have.
- A `objcect` is a concrete thing created using the class defination.

#### features
- classes allow code resuablilty
- multiple ojects can be made using the same class


### Real time example
```python
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


```

- `__init__()` is a constructor that runs when an object is created.
- `self` : refers to object being created.
- car1,car2,car3 - Objects(instance.)

#### Real-Time Implementation

- class Driver -> name , rating, location
- each object  will have different values.

1. Explain the concept
2. Real world world
3. Code and explain
4. Real time implementation
5. When to use.
6. where to use.
7. how to memorize (interview
8. shortcut to understand
9. coding interview questions.)


#### when to use
- when you need to model `multiple similar objects`.
- This is kind of organizing the code.

#### memory tip :

## `__init__` Method and `self` Keyword

- `__init__` : A constructor method that is called automatically when a class object is created.
- `self` : A reference  to the current instance of the class (used to access variables and methods)

___
- `__init__` sets up the object with default or passed -in values.
- `self` is like `this object` . It allows object-specific data access inside the class.
---
- `__init__`is just on of the pythons "dunder" (double underscore method) 
- `self` must always be the first argument in any instance method

---
- [❌] Topic 3 : instamce variable vs class Variables.
- [❌] Topic 4 : Types of Methods in Python Classes
- [✅] Topic 5 : Encapsulation
- [✅] Topic 6 : Inheritance 
- [✅] Topic 7 : Polymorphism 
- [✅] Topic 8 : Abstraction
- [⚠️] Topic 11 : Solid principles


## Encapsulation

Encapsulation in oop concept of `hiding internal object details` from the outside world and controlling access to data through `methods or properties`.

Eg: ATM (Encapsulated)
- withdraw , deposit money using button ( limited acccess which are required ). a part from this you can't directly access money.

- `public` members - accessing from anywhere.
- `protected members` - intented to use internally.
- `Private` - 

Encapsulation make sure that `sensitive data is not directly modified` but accessed through controlled interfaces like getter and setters

```python


class BankAccount:
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        
        
    def deposit(self, amount):
        
        self.balance += amount
        print(f"{amount} deposited sucessfully to {self.holder}")
        return self.balance
    
    def withdraw(self,amount):
        if amount < self.balance :
            self.balance -=amount
            print(f"{amount} withdraw successfully")
            print(f"remaining balance{self.balance}")
        else:
            print("Insufficient balance")
        
        
        
tarun_account = BankAccount("tarun",15000000)

print(f"account holder name : {tarun_account.holder}")
print(f"account balance : {tarun_account.__balance}")

tarun_account.deposit(100)

print(f"account balance after deposit : {tarun_account.balance}")
praveen_accont = BankAccount("praveen something ", 2)


print(f"account holder name : {praveen_accont.holder}")
print(f"account balance : {praveen_accont.balance}")


print(f"account balance : {tarun_account.balance}")


teja_account = BankAccount("teja",500000)

teja_account.withdraw(20)

print(teja_account.balance)

print(teja_account.withdraw(9000))
```

- Encapsulation : hidding data + controlling access to it


## Inheritance 
- Inheritance allows a class (child)  to `inherit properties and methods` from another class(parents), to promote `code resuability`

- A child class is a `specilized version of a parent class`

- A child class automatically gets the parenst's:
    - Variable (attributes)
    - Function (methods)


```python

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


```


```Python
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
        print(f"{self.name} is navigating to the location")

# Rider
class Rider(User):
    
    def request_ride(self):
        print(f"{self.name} is requesting a ride.")
        
        
Driver1 = Drive("tarun")
Rider1  = Rider("teja")


Driver1.login()


Rider1.login()

Rider1.request_ride()

Driver1.navigate()

```

### when to use 

- when multiple classess shares `common functionalities`.
- to extend a class for `specific behaviour`.
- To implements `DRY` (Don't Repeat yourself)


### where to use
- Game dev : - Base character - > enemy , player 
- webdevelopment - Base -> admin, employee 


> `Child copies parent`

[❌] overriding 
[❌] Multiple inheritance, multi level , single inheritance


## Ploymorphism
- Ploymorphism means `many forms` in OOP, it refers to the ability to use `the same method or operation in different ways` depending on the object.

- ploymorphism allows functions / methods to `work differently` for different data types are classes


----

Any programming language - Python ( basic core concepts + OOPs)
- django (frame work  for webdevelopment ) - application to show 
- SQL

- Appitude amd reasoning
- Coding skills (Hacker Rank - low and medium level questions is enough till oops)  ❌ DSA
- Communication skiils ( you have to tell the definations as it is , don't try to recreate the definations)

- Interview preparation is must. 

- Digital protifolio ( html css and js )
- Exhibiting the skills in social media (LN)



## Abstraction
- Abstraction is the oops concept of `hiding complex implementation details` and showing only the `essential features` of an object.

- abstraction will let you `focus on what an object does`, not how it does.

- in python Abstraction can be achieved through :
 - `Abstract Base Classes (ABC)`


- it forces child class to `implement cretain methods` , making your code `standardized and consistent`


Eg : TV remote - press the button on/off -> on/ off the TV ->

- do you know how it works ? - do you think about signals and inner codes or the funcationality wheather its on or off ?


- car you know how to drive a car - but do you really think of which cylinder is moving fast - how heat is transfered. we just think of driving on the road not how engines internally works ?

- ATM - we think of withdraw - not how system is going to dispatch the logic


> Users sees WHAT to do , not HOW it works internally.



```Python 


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
    

```


### When to use 
- when multiple classes shares the same interfaces but different in behaviour




## modules and packages 

### What is module ?
- A Module is just a file that contains python code

eg: You have a library -> contains books 
    python module      -> contains lines of code 
    tool box           -> tools
    Folder contains    -> files

same in python - we split code into modules  -> to keep the things clean and resuable.

- A module is a `.py` file containing variables, functions , or classes 


#### packages 
A package is a folder containing multiple modules