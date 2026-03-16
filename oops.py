#Reverse a string without using [::-1]
print()
stri = "praveen"
st = ""
for i in stri:
    st = i + st
    
    
print(st)

print()


# madam

st = "madsam"



left = 0
right = len(st)-1

while left < right :
    if st[left] != st[right]:
        print("not palindrome")
        break
    left +=1
    right -=1
else :
    print("palindrome")   
print()

#Find the first non-repeating character in a string

stri = "progrpamming"


for char in stri:
    if stri.count(char) == 1:
        print(char)
        break