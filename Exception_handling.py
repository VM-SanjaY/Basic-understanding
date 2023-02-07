# there are three type of errors
# 1 Compile error
# 2 Logical error
# 3 Run time error

# syntax for Exception handling
# try(run the code) -> except(error message or exception) -> else(No exception? run this code) -> finally(always run this code)


#  ***********  Key notes  ***********
# you can write try block without any except blocks.
# you can write several except block for a single try block.
# you can write multiple except blocks to handle multiple exceptions.
# you can write exception as an object.
# you can write multiple exception within tuple.
# in except block you can write different code also like if and else.
# you can use else to see whether any exception is there as it will not run if any exception is present.

# Different types of exceptions -- :::type exactly as it is, this check whether this error is there or not.


# 1) ZeroDivisionError as zd

a = 5
b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError as zd:  # by mention the error category at start it checks for this error alone.
    print("You are trying to divide a number by zero")
    print(zd)


# 2) Exception as ex

a = 10
b = 0
try:
    print(a/b)
except Exception as ex:
    print("there is a error and it is",ex )  # this mentions what error is happening


# 3) NameError as  na

a = input("what is your name: ")
c = ("Your name is",a)
try:
    print(d)
except NameError as na:
    print("wrong variable is mentioned in the try block")
    print(na) # this says what is the mistake


# 4) TypeError as te

a = "45"
b = 5
try:
    c = a + b
    print(c)
except TypeError as te:
    print("type error")
    print(te)


# 5) SyntaxError

# 6) IndentationError

# 7) AssertionError

# 8) FileNotFoundError

# 9) userdefined error   -  error condition we create

# user defined error is create  using raise method

class InvalidData(Exception):
    pass
marks = int(input("Enter the marks: "))
try:
    if marks <0 or marks>100:
        raise InvalidData
except InvalidData:
    print("marks should be between 0 to 100")




































