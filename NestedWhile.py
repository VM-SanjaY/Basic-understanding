# How does a nested for work is
# 1) first it iterates the first index and then it moves to the second loop where the same index is
#    iterated letter by letter.
# 2) outer for loop can have inner while loop and outer while loop can have inner for loop.

# Basic nested While loop

a = 11
while a >0:
    b = 11
    while b> a:
        print("*",end=" ")
        b = b-1
    a=a-1
    print()
# ------------------------------------------------------------------------------------------------
# For loop within a while loop   # perfect number
x = int(input("Mention a range from which you want the perfect numbers: "))

a = 1
while a <= x:
    sum =0
    for i in range(1,a):
        if a%i==0:
            sum =sum+i
    if sum ==a:
        print("perfect number: ",a)
    a=a+1

# ------------------------------------------------------------------------------------------------







