# lambda is similar to def function

# syntax for lambda

# lambda( arguments ):expression

# function                                 |      lambda function
#                                          |
# def add(a,b):                            |   add = lambda a,b:a+b
#     return a+b                           |
# add(3,8)                                 | print(add(3,8))
from functools import reduce

# add in lambda
add = lambda a,b:a+b
print(add(5,10))

# sub in lambda
sub = lambda a,b:a-b
print(sub(10,5))

# multiply in lambda
mul = lambda a,b:a*b
print(mul(10,2))

# divisible in lambda
div = lambda a,b:a//b
print(div(44,4))

# adding and subtracting
addsub = lambda a,b,c:a+b-c
print(addsub(14,15,6))

# *args  usage in lambda
addition = lambda *args: sum(args)   # using args we can put a lot of parameters
print(addition(10,20,5,15,20,100,18))

# odd or even in lambda
check = lambda x: (x%2 and "odd" or "even")
print(check(87))

# lambda using filter
num = [10,50,80,60,20,30,55,44,33,22]
great = list(filter(lambda num: num>40, num))
print(great)

# is the number divisible by 5
num = [10,50,80,60,20,30,55,44,33,22]
divisi = list(filter(lambda num: num%5 == 0, num))
print(divisi)

# is the number not divisible by 5
num = [10,50,80,60,20,30,55,44,33,22]
divisi = list(filter(lambda num: num%5, num))
print(divisi)

w = [1,2,2,4,5,6,7,3,8]
double = list(map(lambda x : x*2,w))
print(double)

# cube power
need_powa = [2,3,4,5,9,7]
cube = list(map(lambda x:pow(x,3),need_powa))
print(cube)

# using reduce   # it provides a sum of all the digits inside.
sum = [2,2,2,2,2,4,4,4,4]
sum_of = reduce((lambda x,y:x+y),sum)
print(sum_of)


# fractorials

y = []
inp = int(input("Enter a number: "))
for i in range(1,inp+1):
    y.append(i)
print(list(reversed(y)))

fact = reduce((lambda a,b:a*b),y)
print(fact)



















