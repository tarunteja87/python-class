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