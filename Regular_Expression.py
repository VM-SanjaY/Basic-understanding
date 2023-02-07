# Regular Expression
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Regular expression is used for pattern recognition, character recognition and
# to identify different sequence of character
# ^ and $ are called Metacharacters
# list of Metacharacters [].^$*+?{}()\|

# square brackets []  - they are used for specify a set of characters you wish to match
# [abc] checks whether any character is present in a text. and when there is a space in text it ends there and
# does not look into the next word.


import re  # re is short for regular expression

# Example 1
pattern = '^a...s$'           # This check whether any text matches with the mentioned pattern
test_string = "alias"         # that is thw word starts with a and has 5 character in between and ends with s
result = re.match(pattern,test_string)

if result:
    print("match successful")
else:
    print("match unsuccessful")


# Example 2

name = input("what is your name: ")
patt = "^......$"       # you don't have to mention the start and end character.
result = re.match(patt,name) #

if result:
    print("As your name say you must be great")
else:
    print("you must be average")

txt = "The rain in Spain"                    # search and match are almost same.
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

# Example 3 with compile

pattern = re.compile(r"")
while True:
    password = input("Please enter a password")
    if len(password)<6:
        print("Your password should contain at least 6 character")
    elif re.search(r"[!@#$%&]",password) is None:
        print("your password must contain at least a special character")
    elif re.search(r"\d",password) is None:
        print("Your password should contain at least one number")
    elif re.search(r"[A-Z]",password) is None:
        print("Your password should contain at least one Capital letter")
    elif len(password)==6:
        print("password strength is weak")


    else:
        print("Password Created Successful")
        break

print(password)































