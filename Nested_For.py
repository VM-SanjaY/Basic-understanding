# How does a nested for work is
# 1) first it iterates the first index and then it moves to the second loop where the same index is
#    iterated letter by letter.
# 2) outer for loop can have inner while loop and outer while loop can have inner for loop.

#Syntax   1                                   |                   syntax 2
#Outer loop:                                  |                   outer loop:
#    inner loop:                              |                         statement for outer loop
#       statement for inner loop              |                          inner loop
#    statement for outer loop                 |                                statement for inner loop

#------------------------------------------------------------------------------------------------------------------

# Example
x = ["Nested", "For", "in", "workings"]

for i in x:
    print("The outer loop -", i)
    for letter in i:
        print("innerloop - ",letter)

# ----------------------------------------------------------------------------------------------------------------
# Basic nested for loop
# Type 1
x = ["Nested", "For", "in", "workings"]

for i in x:
    for letter in i:
        print(letter, end="*")
    print()

# Type 2              Know the difference

x = ["Nested", "For", "in", "workings"]

for i in x:
    for letter in i:
        print(letter, end="*")


# -----------------------------------------------------------------------------------------------------------------

# using two list
fruits = ["green apple","banana","orange","sweet lime"]
vegetable = ["tomato","onion","carrot","potato"]

for fruit in fruits:
    for veg in vegetable:
        print(fruit,veg)
    print()

# ------------------------------------------------------------------------------------------------

# Square pattern

x = int(input("Mention a number: "))
y = input("Mention a symbol you want it to print: ")
for i in range(x):
    for j in range(x):
        print(y,end="")
    print()

# --------------------------------------------------------------------------------------------------

# right angle triangle

x = int(input("Mention a number: "))
y = input("Mention a symbol you want it to print: ")
for i in range(x+1):
    print("", end="")
    for j in range(i):
        print(y,end="")
    print()
# -----------------------------------------------------------------------------------------------

# adding two list to an empty list
# type 1
a=[1,2,3,4]
b=[5,6,7,8]
c=[]
for i in a:
    for j in b:
        c.append(i+j)
print(c)                     # this will get result as 1+5,1+6,1+7........

# type 2
a=[1,2,3,4]
b=[5,6,7,8]
c=[]
for i in a:
    for j in b:
        c.append(i)
        c.append(j)
print(c)                    # this will give 1,5,1,6,1,7...........

# type 3

a=[1,2,3,4]
b=[5,6,7,8]
c=[]
for i in a:
    for j in b:
        c.append(j-i)
print(c)                               # This will give the result as 4,5,6,7,3,4,2...........

# ---------------------------------------------------------------------------------------------

#  While in for loop

fruits = ["green_apple","orange","Water_melon"]
for fruit in fruits:
    a=0
    while a<5:
        print(fruit,end=" ")
        a=a+1
    print()

# -----------------------------------------------------------------------------------------------













