# ******      tuples      ******#
# tuple is a collection of immutable heterogeneous python objects and list is mutable, that is once a variable is
# set for tuple it can not be change in the middle like list where we can append or extend. it cannot be used
# here as it changes the old version of it.

# empty tuple
a = ()
print(type(a))
print(a)

# ----------------------------------------------------------------------------------------------------------
# Working of index in tuple - It is same as list.

a = ("a","b","c",1,2,3)
print(type(a))
print(a[2])

# another way # bracket is not necessary it can be written without it.

b = "a", "b", "c", 1, 2, 3
print(type(b))
print(a[4])

# ------------------------------------------------------------------------------------------------------------

# Concat is available in tuple.

a = ("a","c","d")
b = 1,2,3,4
c = a+b
print(type(c))
print(c)

# -------------------------------------------------------------------------------------------------------------

# Nested tuple

a = ("a","c","d")
b = 1,2,3,4
c=(a,b)
print(c)

# -------------------------------------------------------------------------------------------------------------

# repetition

a = 0,

print(a*100)
print(type(a))

# this does not store a = 00000..... like list "a" will always be "0,"

# ------------------------------------------------------------------------------------------------------------

# if you want all the character of a word as tuple   -------  Un Packing -------

# type 1
a = tuple("hello")
print(a)

# type2

num = (1,2,3,4,5)

a,b,c,d,e=num
print(a)
print(c)

# type 3

num = (1,2,3,4,5)

a,*b,d,e=num
print(a)
print(c)
print(a,b,d,e)

# ------------------------------------------------------------------------------------------------------------

# Delete =   we can delete a tuple but cannot remove a world inside a tuple like in list.

a = 1,2,3,4,5,
print(a)
del a
#print(a)

# -------------------------------------------------------------------------------------------------------------

# len

a = (1,2,3,4,5,6,)
print(len(a))

# -------------------------------------------------------------------------------------------------------------

# sum

a = (1,2,3,4,5,6,7,8)
print(sum(a))

# -------------------------------------------------------------------------------------------------------------

# count

a = (1,2,3,3,3,3,4,5,8,8,8,8,8,8,9,9,7,52,3)
print(a.count(8))

# --------------------------------------------------------------------------------------------------------------

# min and Max

a = (1,2,3,4,58,14,56,700)
print(min(a))
print(max(a))

# -----------------------------------------------------------------------------------------------------------------

# converting list to tuples      -        but tuple cannot be converted to list

a = [1,2,3,4]
b=tuple(a)
print(b)
print("a = ",type(a),",","b = ",type(b))

# ---------------------------------------------------------------------------------------------------------------

# nested tuple in list            ## this way you can use append and extend to add another list

a = [(1,2,3,4),("a","b","c","a")]

a.append((1,"a"))
print(a)

# --------------------------------------------------------------------------------------------------------------

# nested list in tuple

a = ([1,2,3],["a","b","c"])   # in this you cannot add anything to the tuple like adding extra list
# but you can add stuff to the list in side the tuple
a[0].append(4)
print(a)
b = ["d", "e", "e", "g", "h"]
a[1].extend(b)
print(a)

# ---------------------------------------------------------------------------------------------------------

# range

a = tuple(range(1,11))
print(a)

# ---------------------------------------------------------------------------------------------------------



