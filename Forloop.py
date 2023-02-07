#                  ------------     For Loop    -------------

#Basic for loop

a = ["a","b","c","d"]
for i in a:
    print(i)
# -----------------------------------------------------------------------------------------------------------

# for in range

for i in range(1,11,1):  #(1 is the start point, 11 is the end point last no excluded, 1 is the movement or interate point)
    print(i, end=" ")   # end="" avoid new newline when interated and if new line need use /n

# ----------------------------------------------------------------------------------------------------------------
# Sum

d = int(input("Number: "))
series = int(input("Till where you want the sum of: "))
s = 0
for i in range(1,series+1):
    s = s+d
print("Total of the sum of the number is ",s)


# ----------------------------------------------------------------------------------------------------------------
# multiplication table

C = int(input("Enter the number you want the multiplication table of : " ))
X = int(input("Till where you want to see: "))
for i in range(1, X+1):
    print(C, "x", i, "=", C*i)

# -----------------------------------------------------------------------------------------------------------------

# division table

D = int(input("Enter the number you want the Division table of : " ))
X = int(input("Till where you want to see: "))
for i in range(1, X+1):
    print(D*i, "/", D, "=", round((D*i)/D))

# ----------------------------------------------------------------------------------------------------------

# Square table

X = int(input("Till where you want to see square: "))
for i in range(1, X+1):
    print(i,"^2", "=", i**2)


# -------------------------------------------------------------------------------------------------------------
# calculating len of a list using for loop

x = [1,2,3,4,5]
count = 0
for i in x:
    count +=1
print(count)

# -----------------------------------------------------------------------------------------------------------
# for loop using range and len
a = ["san","kar","Mal","vij","Vis"]
for i in range(len(a)):
    print("hello ", a[i])

# ----------------------------------------------------------------------------------------------------------

# find the maximum value without using max function

student_scores = [1,2,3,7,8,4,5]
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print("The highest score in the class is: ",high_score)

# ---------------------------------------------------------------------------------------------------------------
# find the minimum value without using max function

student_scores = [6,2,3,7,8,4,5]
lowest_score = student_scores[0]
for score in student_scores:
    if score < lowest_score:
        lowest_score = score
print("The highest score in the class is: ",lowest_score)

# -------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------

# Average    ********************* this uses both while and for  ***********************************

n = []

while True:
    number = int(input("Type the number here: "))
    n.append(number)
    Result = input("Do you want to enter another number: Y or N ")
    Result.lower()
    if Result == "n":
        break
    elif Result == "y":
        continue
    else:
        break
s = 0
for i in range(len(n)):
    s = s+n[i]
average = round(s/len(n),2)
print("The to total average of",s,"by",len(n),"is",average)

# ---------------------------------------------------------------------------------------------------------------

# else    = We can use an else clause after the for.

for i in range(1,4):
    print(i)
else:
    print("it will print this message at the end irrespective of it successful or not")

# ----------------------------------------------------------------------------------------------------------------
# Break   = This stops or breaks the loop at assigned point or condition point

for i in range(1,10):
    if i==7:
        break
    print(i)     # this will print till 6 and stop

# -----------------------------------------------------------------------------------------------------------------
# Continue   = This will skip only the condition and print all of them.

for i in range(1,10):
    if i == 7:
        continue
    print(i)      # This will print 1,2,3,4,5,6 and then skip(7), print remaining 8,9

# -----------------------------------------------------------------------------------------------------------------
# Cube root

x = [1,2,3,4,5,6,7,8,9,10]
cube = []
for i in x:
    cube.append(i**3)
print(cube)

# -----------------------------------------------------------------------------------------------------------------
# Zip function

fruits = ["apple","orange","lemon"]
grammar = ["is","is","is","is"]
colour = ["green","orange","yellow"]

for i in zip(fruits,grammar,colour):
    print(i)

# -----------------------------------------------------------------------------------------------------------------

# for loop using split
# input should be like this  10 20 30 40 50 60

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)


