
"""

################ Write ###################

file = open("test.txt", "w")


file.write(" hello students this is writing from the code")


file.close()




###### Append #######

file = open("test.txt", "a")

file.write("\nthis is appended text ")

file.close()


###########  READ ##############

file = open("test.txt", "r")  # open the file in read mode.

content = file.read()  # read the content of the file.

print(content)  # print the content of the file.

file.close()  # This is the important step when you use open function


"""


file = open("text.txt","w")

file.write("hello this is the file created using open function in python")

file.close()


