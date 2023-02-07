# ************************        Dictionary        ***************************
# dictionary are key value pair, which are called out by the key or item.
# Dictionary is written within {}, dict({}) and dict([(),(),()...])
# item is used to call out both key and value.
# in dictionary key can both integers and strings

# basic dictionary

d = {1:"Hello",2:"Hi",3:"Bye"}
print(d)
print(type(d))

# ------------------------------------------------------------------------------------------------
# another way of typing
d = dict({1:"Hello",2:"Hi",3:"Bye"})
print(d)
print(type(d))

# 2
d = dict([(1,"Hi"),(2,"Hello"),(3,"Bye")])
print(d)
print(type(d))

# -------------------------------------------------------------------------------------------------
# nested dictionary

d = {"name":{"firstname":"sanjay","last name":"V M"},"age":25}
print(d)
print(type(d))

# -------------------------------------------------------------------------------------------------
#  adding datat into a empty dictionary

d = {}

d[0]="hello"               #  using integers as key value
print(d)

d["name"]="sanjay"
print(d)
print(type(d))

# updating the existing name

d["name"]="ken"
print(d)

# -------------------------------------------------------------------------------------------------
# Accessing the values from a dictionary

d = {"name":{"firstname":"sanjay","last name":"V M"},"age":25}

print(d["name"])                    # it is used to call out the value using their key.
print(d["name"]["firstname"])       # you can access the inner nest using this method.
print(d.get("name"))                # This is another method to call out a value using key.
# -------------------------------------------------------------------------------------------------
# Deleting the key and values in a dictionary.

# pop method
d = dict([(1,"Hi"),(2,"Hello"),(3,"Bye")])
d.pop(1)                          # this method deletes the mentioned key.
print(d)

# popitem method
d.popitem()                       # This method deletes the last key in the list.
print(d)

# ------------------------------------------------------------------------------------------------

# To check only the values of the dictionary

d = {1:"Hello",2:"Hi",3:"Bye"}

print(d.values())


# to check keys

print(d.keys())

# -------------------------------------------------------------------------------------------------

# Fromkeys method

keys={"a","b","c","d"}
value=1
a = dict.fromkeys(keys,value)
print(a)

# -------------------------------------------------------------------------------------------------

# Clear method                 This method deletes all the data in the dictionary

a.clear()
print(a)

# ----------------------------------------------------------------------------------------------------------------
#dictionary in new line using for loop

dict = {}
sub = 5
i = 0
while i < sub:
    name = input("enter the subject ").capitalize()
    mark = int(input("enter the mark "))
    i = i + 1
    dict[name] = mark

print(dict)
for key, value in dict.items():
    print(f"{key}:{value}")


# -----------------------------------------------------------------------------------------------------------------






# -------------------------------------------------------------------------------------------------

#     *****************************           Set         **********************************

# set is ann unordered collection of unique elements.
# set is iterable and can be mutable and immutable

# syntax == variable_name = set(["a","b","c"])    ===> result will be printed out in {"a","b","c"}


# BASIC SET EXAMPLE

s = set([1,2,3,4])

print(s)

# --------------------------------------------------------------------------------------------------------------------
# adding values to a set

se = set(["a","b","c"])
se.add(1)
print(se)

# -------------------------------------------------------------------------------------------------------------------

# frozenset  it is immutable

s = frozenset([1,2,3])
print(s)
print(type(s))

# ----------------------------------------------------------------------------------------------------------------

# union            # they add two sets and remove duplicates when printing

a = set([1,2,3,4,5,6])
b = set([1,3,7,8,9])
c = a.union(b)
print(c)

# -----------------------------------------------------------------------------------------------------------------

#  Difference                       # this provides the difference in the set1 compared to set2

a = set([1,2,3,4,5,6])
b = set([1,3,7,8,9])

c=a.difference(b)                   # what is the difference of a when compared to b
print(c)

# ---------------------------------------------------------------------------------------------------------------

# operators                         # We can use operators in set

a = set([1,2,3,4,5,6])
b = set([10,8,7,8,9,10])

print(a==b)
print(b>a)
print(b<a)
print(10 in b)
print(10 not in a)
# print(a+b)          # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(a-b)          # TypeError: unsupported operand type(s) for -: 'set' and 'set'

# -----------------------------------------------------------------------------------------------------------------

# Exclusive operator   = "^"          # this operator shows the uncommon values in both the sets.

a = set([1,2,3,4])
b = set([1,2,5,6])

print(a^b)             # result will be  = {3,4,5,6}

# ------------------------------------------------------------------------------------------------------------------
# remove a value in set

x = set([1,2,3,4,5])
print(type(x))
x.remove(2)
print(x)


