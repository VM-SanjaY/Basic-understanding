# ************************   While Loop *******************************

# Basic While loop.

a = 0                      # always set a value
while a <10:               # set a condition
    a = a+1                # Who does it have to run
    print(a)               # Print what you need

# ----------------------------------------------------------------------------------------------------------------

# Printing a sentence in loop

a = 0
while a < 5:
    print("I am a player")
    a = a+1
# ------------------------------------------------------------------------------------------------------------------
# using Break

# Type 1
a = 0
while a<5:
    print("Lets see")
    a=a+1
    if a ==4:
        break
                           # -------------------- #
# Type 2
a =0
while True:
    name = input("May I know your name: \n")
    name.lower()
    if name == "sanjay":
        break
print("Ahh you know your spelling")


# ---------------------------------------------------------------------------------------------------------------

# continue     -    # Continue is different in while compare to for
# type 1
a = 0
while a <10:
    a = a+2
    print("Believe")
    if a == 8:
        print("you can")
        continue

# Type 2

a = 0
while a<10:
    a+=1
    if a ==6:    # in this 6 is skipped
        continue
    print(a)


# ------------------------------------------------------------------------------------------------------------------
# LCM

x = int(input("mention the first number "))

y = int(input("mention the second number: "))
a = 0

while True:
    a += 1
    if not (a%x or a%y):
        break
print(a)

# ------------------------------------------------------------------------------------------------------------------

# else in while

a= 0
while a< 4:
    a+=1
    print(a)
else:
    print("Over")

# ------------------------------------------------------------------------------------------------------------------
# pop deletes or remove the data in a list.

a = [1,2,3,4,5,6]
while a:
    print(a.pop())
else:
    print("over")
print(a)

# -----------------------------------------------------------------------------------------------------------------
# avg

n = 0
sum = 0
count = 0

while n >= 0:
    n = int(input("Please mention a number "))

    if n >= 0:
        count = count + 1
        sum = sum + n
avg = sum / count
print("Total is", sum, "Count is", count, "Average is", avg)

# -------------------------------------------------------------------------------------------------------------
# Number guessing game

import random
print("Number guessing game")
x = random.randint(1,100)
print(x)
n = 0
while n >= 0:
    n = int(input("Mention a number"))
    if n == x:
        print("you have guessed the number right")
        break
    elif n < x:
        print("Type a number higher than this")
        continue
    elif n >x:
        print("Type a number lower than this")
        continue






