### Step 1:

number1 = int(input("Enter first number1 : "))
number2 = int(input("Enter first number2 : "))
operator = input("Enter operator : ")


### Step 2 :


def add(number1, number2):
    return number1 +  number2

def sub(number1, number2):
    return number1 -  number2
 
def multiply(number1, number2):
    return number1 *  number2
 
def divide(number1, number2):
    return number1 /  number2
 
 
#### step 3

 
if operator == "add" :
    print("addition of two numbers is : ")
    print(add(number1, number2))
    
if operator == "sub" :
    print("subtraction of two numbers is : ")
    print(sub(number1, number2))
    
if operator == "multiply" :
    print("multiplication of two numbers is : ")
    print(multiply(number1, number2))
    
if operator == "div" :
    print("division of two numbers is : ")
    print(divide(number1, number2))
    
    
if operator == "":
    print("Invalid operator")
    
    print("addition of two numbers is : ")
    print(add(number1, number2))
    
    print("subtraction of two numbers is : ")
    print(sub(number1, number2))
    
    print("multiplication of two numbers is : ")
    print(multiply(number1, number2))
    
    print("division of two numbers is : ")
    print(divide(number1, number2))