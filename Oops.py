# Object-oriented programming (OOP) is a method of structuring a program by
# bundling related properties and behaviors into individual objects.
# oop is used by typing the word - "class" and the word should be capitalized
# instance attribute : is defined in __init__(self)



# there are four principles of oops
# 1) Inheritance
# 2) Polymorphism
# 3) encapsulation
# 4) Abstraction

# Example - we are going to create a class you few parameter
'''
# position, firstname, lastname, age, level salary
se1 = ["Developer", "sanjay","VM",25,"junior",25000]
se2 = ["Developer", "Ram","Kumar",23,"Junior",21000]
# class
class Developer:
    alias = "Designer"
    def __init__(self,firstname,lastname,age,level,salary):
        self.firstname=firstname
        self.lastname=lastname  # self is called instance attribute
        self.age=age
        self.level=level
        self.salary=salary


    def code(self): # self is used to call the details stored above
        print(f"{self.firstname} is writing a code")  # to call this
    def code_language(self,language):
        print(f"{self.firstname} is writing a code in {language}")
    # __  __ method
    def __str__(self):
        information = f'{self.firstname},{self.lastname},{self.age},{self.level},{self.salary}'
        return information
    def entry_salary(age):
        if age < 25:
            return 25000
        elif age < 30:
            return 30000
        else:
            return "you are too old for this"

se1 = Developer("sanjay","VM",25,"junior",25000)    # instance
se2 = Developer("Ram","Kumar",23,"Junior",21000)

print(se1.firstname, se2.lastname)
se1.code()
se1.code_language("python")
# print(Developer.firstname) # will throw an error as it is only fixed to an instance and not the class
print(Developer.alias) # THIS WORKS BECAUSE IT IS NOT INSIDE THE INSTANCE CLAUSE
print(se1.alias) # this also works
print(se1)  # __str__ is used here
# if you do not want the self parameter for calling those you need to use the classname.function(parameter)
# print(se1.entry_salary(24)) # TypeError: Developer.entry_salary() takes 1 positional argument but 2 were given
print(Developer.entry_salary(35)) # this will work because self will automatically be used even if you don't mention it

# inheritance
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Developer(Employee):
    pass
class Tester(Employee):
    pass

dev = Developer("Sanjay",25)
tes = Tester("Ben",28)
print(dev.name,tes.age)
'''
# ----------------------     There are some change     ----------------------
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

class Developer(Employee):
    def __init__(self,name,age,salary,level):
        super().__init__(name,age,salary) # this is used to drag the above-mentioned initializer __init__(Employee)
        self.level = level

class Tester(Employee):
    pass

dev = Developer("Sanjay",25,25000,"junior")
tes = Tester("Ben",28,30000)
print(dev.name,tes.age,tes.salary,dev.level)

# Polymorphism  - many shape it helps to use class exactly like it parent class








