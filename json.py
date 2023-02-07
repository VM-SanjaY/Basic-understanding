# Json = JavaScript Object Notation is used for transmitting data in web applications
# sending some data from the server to the client, so it can be displayed on a web page, or vice versa
# json is written like dictionary key value pairs

import json

person = {"name":"sanjay","age":25,"company":["RRD","Colan"],"skill":["python","sql","alteryx","excel"],"employed":True}
person_json = json.dumps(person, sort_keys=True) # sort key sort the output in alphabetical order
person_json = json.dumps(person,indent=4, separators=(" ; "," = ")) # the separators are used for
print(person_json) # to change , to ; and : to =  # mostly don't use separators

# write it to a json file   # difference between s and no s at the end is to differentiate it from file
# and code
with open("person.json","w") as file:
    json.dump(person,file,indent=4)

# deserialization or decoding   turning json file to python file
load = json.loads(person_json)
print(load) # avoid using separator when loading it back

# load is used to load a json file as readable in python
with open("person.json","r") as file:
    load = json.load(file)
print(load)



# Writing a json using class method
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User('sanjay',25)

def encode_user(o):
    if isinstance(o,User):
        return {"name":o.name,"age": o.age, o.__class__.__name__:True }
    else:
        raise TypeError('Object of type User is not Json serializable')

userJSON = json.dumps(user, default = encode_user, indent=4)
print(userJSON)


# DECODE IT USE TO derive the data needed from the file
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"],age=dct["age"])
    return dct

user = json.loads(userJSON,object_hook=decode_user)  # HOOK IS USED TO PULL THE CODE FROM THE FUNCTION
print(user.name)
print(type(user))












