number1 =  int(input("enter number 1 : "))
number2 =  int(input("enter number 2 : "))

operation = input("Enter the operations : ")

def add(number1,number2):
    print(f"addition of {number1},{number2} is {number1+number2}")
    return number1+number2

def substract(number1,number2):
    print(f"substraction of {number1},{number2} is {number1-number2}")
    return number1-number2

def multiply(number1,number2):
    print(f"multiplication of {number1},{number2} is {number1*number2}")
    return number1*number2


def divide(number1,number2):
    print(f"division of {number1},{number2} is {number1/number2}")
    return number1/number2


if operation == "add":
    add(number1,number2)
elif operation == "substract":
    substract(number1,number2)
elif operation == "multiply":
    multiply(number1,number2)
elif operation == "division":
    divide(number1,number2)
else :
    print("please choose the correct option")
