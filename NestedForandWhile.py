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






