# ******      L i s t   ******#

# list
a=["a", "b","c",1,2,3]
print(a)
# --------------------------------------------------------------------------------------------------------------
# nested list
#type 1

a = [[1,2,3],["a","b","c"]]
print(a)

#type 2
a = [1,2,3,]
b = ["a","b",'c','d']
c=[a,b]

# ------------------------------------------------------------------------------------------------------
# if you want to type 100 zeroes in a list

a = [0]*100
print(a)
# ----------------------------------------------------------------------------------------------------

# if you print a word as letter in a list

a = list("hello")
print(a)     # result => ["h","e","l","l","o"]
# ------------------------------------------------------------------------------------------------------------------

# append - added character to a list at the end
# TypeError: list.append() takes exactly one argument, it seems we can only add one word or character at the end

a = [1,2,3,4,5]
a.append(6)
print(a)
# ---------------------------------------------------------------------------------------------------------

# use this when you want to separate a list has to.
num = [2,1,3,0,4]
one,two,*other=num
print(one)     # first  index will be printed
print(two)     # second index will be printed
print(other)   # balance rest will be printed * is the wild card
# -------------------------------------------------------------------------------------------------------

#   extend = this is used to add a list or more strings which append fails at the end of another list
a = [1, 2, 3]
b = ["a", "b", "c"]
a.extend(b)
print(a)   # you can add a list
#a.extend("Hello","minna-san")   # TypeError: list.extend() takes exactly one argument this also does not work
#print(a)

# --------------------------------------------------------------------------------------------------------------
# insert   = if you want to insert a list within or in between a list

z = [1,2,3,4,5]
b = ["hello", "Minna-san"]
z.insert(3, "hello")  # (index, what is want to insert)  and assigning a variable is not working.
print(z)
z.insert(3,b) # This also possible
print(z)
# ----------------------------------------------------------------------------------------------------------------

# Remove
a = [1, 4, 5, 6, 2, 38, 4]
b=["a", "b", "c", "d"]
c=[a, b]
a.remove(5) # removing a string inside a list
print(c)
c.remove(b) # removing a list inside a list
print(c)

# -------------------------------------------------------------------------------------------------------------

# sort

a = [4,5,6,1,3]
letter = ["a","b","e","f","c","d"]
letter.sort()
print(letter)

# Sort backwards

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)


# ------------------------------------------------------------------------------------------------------

# len  = finds total length of a list

a = [1, 4, 5, 6, 2, 38, 4]
print(len(a))


# ---------------------------------------------------------------------------------------------------

# min

a = [8,2,3,4,5,6]
print(min(a))
b = ["d","e","g","a"]
print(min(b))

# -------------------------------------------------------------------------------------------------------------
# Max

a = [8,2,3,4,5,6]
print(max(a))
b = ["d","e","g","a"]
print(max(b))

# -------------------------------------------------------------------------------------------------------------
# Sum

a = [8,2,3,4,5,6]
print(sum(a))

# ---------------------------------------------------------------------------------------------------------
# Average

a = [4,5,62,4,3,84,105]

print(sum(a)/len(a))

# ------------------------------------------------------------------------------------------------------------

# range = instead of typing 1 to n number we can use range. last number is excluded

a = list(range(1,11))
print(a)

# --------------------------------------------------------------------------------------------------------------

# list with split
# input should ne like this  10 20 30 40 50 60

student_heights = input("Input a list of student heights ").split()

print(student_heights)

# ----------------------------------------------------------------------------------------------------------------
# taking the input and as strings and converting them as integers

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# ----------------------------------------------------------------------------------------------------------------






