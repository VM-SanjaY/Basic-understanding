# **********        Numpy         ***************
# Numpy is used for scientific and numerical computing.
# Numpy provides high performance multidimensional array objects and tools for working with arrays.
# In numpy the dimensions are called axes.
# In numpy the variable is called vector

# one dimension array : 0 1 2 3 4 5   y(axis) one element  shape:(6,) x(axis) totally 6 six elements

# two dimension array : 0 1 2 3
#                       4 5 6 7   y(axis)two elements  shape:(2,4) x(axis)totally 4 elements

# three dimension array : please look it up as it's hard to draw here


# ****     Example

import numpy as np

a = np.array([1,2,3,4,5]) # just like list you can print the index's = a[0],a[1] like list
print(a)
print(type(a))

# range in numpy
a = np.arange(1,100)     # in numpy its arange and not range
for i in a:
    print(i)

# to check the version
print(np.__version__)

# to check the shape of numpy
a = np.array([1,2,3,4])
print(a.shape)  # or print(np.shape(a)) this also works

# to check the datatype of numpy
a = np.array([1,2,3,4])
print(a.dtype)

# to check the number of dimension of numpy
a = np.array([1,2,3,4])
print(a.ndim)

# to check the size of dimension of numpy
a = np.array([1,2,3,4])
print(a.size)

# to check the itemsize in bytes of dimension of numpy. since it 32byte its 1, if its 64byte it is 2
# for each index
a = np.array([1,2,3,4])
print(a.itemsize)

# if you want to add a number to all in an array
a = np.array([1, 2, 3])
b = a+np.array([4]) # this will add 4 to all the numbers [5,6,7]
print(b)   # this method is called broadcasting
c = a+np.array([4,3,2]) # this will give [5,5,5] as 1+4,2+3,3+2
print(c)  # important note if the array is only 2 that is [4,3] it will throw a ValueError


# using add in numpy
d = np.array([1,2,3,4])
e= d+np.add([5],[10])
print(e)  # provide result like 5+10+1, 5+10+2, 5+10+3 .....

# using append
d = np.array([1,2,3,4])
a = np.append(d,[5])
print(a)

# using math
a = np.array([1,2,3])
b = a+2    # this adds 2 to the 3 numbers in the array
c = a*2    # this multiply 2 to the 3 numbers in the array
d= a/2     # this divide 2 to the 3 numbers in the array
e = a-1    # this subtracts 1 to the 3 numbers in the array
f = np.sqrt(a) # this provides the square root of the array
g = np.square(a) # this provides the square of the array
h = np.log(a)  # this provides the log of the array
print(b,c,d,e,f,g,h)


# dot product method
# normally it is done
l1 = [1,2,3]
l2 = [4,5,6]
dot = 0
for i in range(len(l1)):
    dot += l1[i]*l2[i]
print(dot)
l1 = np.array(l1)    # when using numpy
l2 = np.array(l2)
dot = np.dot(l1,l2)  # this provides the same result has above
print(dot)
dot = (l1*l2).sum()  # this provides the same result has above
print(dot)
dot = l1@l2          # this provides the same result has above
print(dot)
sum1 = l1*l2
dot = np.sum(sum1)   # this provides the same result has above
print(dot)

# ***  *** numpy dimensions ***  ***

# single dimension
a = np.array([1,2,3])
print(a)
print(a.shape)
# 2 dimension
a = np.array([[1,2,3],[3,4,5]])
print(a)
print(a.shape)
# 2 dimension part 2
a = np.array([[1,2,3],[4,5,6],[7,8,9]]) # this will be printed as 3x3
print(a)
print(a.shape)

# how to access data from 2 dimensions
print(a[0,0]) # will print 1 a[y axis,x axis]
print(a[0,1]) # will print 2 a[y axis,x axis]
print(a[2,1]) # will print 8 a[y axis,x axis]

print(a[:,0]) # this will print  the entire y axis
print(a[0,:]) # this will print the entire x axis
print(a.transpose()) # this will transpose the array towards the left
b = a.transpose()
c = b.transpose()
print(c)             # when we do this it goes back to the original data
print(a.diagonal())  # will print the diagonal data
print(a.diagonal(-1)) # this will skip first row and (-2) will skip 2 rows and (-3) 3 wows and goes on
c = np.diag(a)
print(np.diag(c))    # this way we will get diagonal and the remaining places will be replaced with 0

# slicing and indexing od dimensions

a = np.array([[1,2,4,5,6,],[3,4,8,6,4]])
b = a[0,1:4]
print(b) # this will print [2 4 5]
c = a[-1,-1]
print(c) # this will print 4 from backwards
d = a>3
print(d) # this will check whether the data in (a) is greater than 3 or not using boolean
print(a[d]) # this will print all the number that are greater than 3
e = np.where(a<4,a,0)
print(e) # this will provide number <4 and replace the numbers >4 as 0
a = np.array([1,2,3,4,5,6,7,8,9])
b = [1,3,4]
print(a[b]) # in this the list b act as an index and provide the number 2,4,5 as per the index mentioned
even = np.argwhere(a%2).flatten() # this will provide the even number in the list and flatten is used
print(even)                       # to show them in 1 dimension

# shaping in numpy
a = np.arange(1,7)
print(a) # this creates a single dimension array multiple column and single row
b = a.reshape(2,3)
print(b) # this will provide the data in 2 dimensional
c= a[:,np.newaxis]
print(c) # this will provide data in single column and multiple row wise
print(c.shape)
d= a[np.newaxis,:]
print(d) # this also creates a single dimension array multiple column and single row but within another list
print(d.shape)

# concat in numpy
a = np.array([[1,2],[7,8]])
b = np.array([[4,5]])
c = np.concatenate((a,b), axis=0) # and if we change axis to none it will print as single dimension array
print(c) # this will add the data i new line as it is with in a list
d = np.concatenate((a, b.transpose()), axis=1)
print(d)  # This prints the data in the column way that is there will be three columns and two row.

# hstack

a = np.array([1,2])
b = np.array([4,5])
c=np.hstack((a,b))
print(c)  # this will print the data in horizontal way
a = np.array([1,2])
b = np.array([5,6])
d = np.vstack((a,b))
print(d) # this will print the data in vertical way

# broadcasting

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([1,0,1])
x = a+b
print(x)   # this add 1,0,1 to all the data in the order of 1+1,2+0,3+1 4+1,5+0,6+1 ..............

# functions in numpy

# sum
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.sum()) # this provides the sum of all the data in the matrix at start it is always axis = none
print(a.sum(axis=0)) # this adds all the data in column format that is 1+4+7 = 12, 2+5+8= 15......
print(a.sum(axis=1)) # this adds all the data in the row that is 1+2+3 = 6, 4+5+6 = 15 .......

# mean
a = np.array([[1,2,3],[4,5,6]])
print(a.mean())
print(a.mean(axis=0)) # this provides means all the data in column
print(a.mean(axis=1)) # this provides means all the data in row


# average
a = np.array([[1,2,3],[4,5,6]])
print(len(a))
print(a/len(a))

# variation
a = np.array([[1,2,3],[4,5,6]])
print(a.var())
print(a.var(axis=0)) # this provides variation all the data in column
print(a.var(axis=1)) # this provides variation all the data in row

# standard deviation
a = np.array([[1,2,3],[7,8,9]])
print(a.std())
print(a.std(axis=0)) # this provides standard deviation all the data in column
print(a.std(axis=1)) # this provides variation all the data in row

# minimum
a = np.array([[1,2,3],[7,8,9]])
print(a.min())
print(a.min(axis=0)) # this provides minimum all the data in column
print(a.min(axis=1)) # this provides minimum all the data in row

# maximum
a = np.array([[1,2,3],[7,8,9]])
print(a.max())
print(a.max(axis=0)) # this provides maximum all the data in column
print(a.max(axis=1)) # this provides maximum all the data in row

# datatype

x = np.array([1,2])
d = x.dtype=np.int64
print(x.dtype)  # we can change the data type assign a datatype to it

# copying and assigning
a = np.array([1,2,3,4])
b = a
b[0] = 15
print(b)  # even though we have made change to the copy (b) when trying to print (a) it will also provide
print(a)  # the same result as (b) as the both points to the same location of the data so change made to
          # one will reflect on others as well
          # but we can avoid this issue
a = np.array([1,2,3,4])
b = a.copy()  # that problem can be resolved using this method
b[0] = 15
print(b)
print(a)

# generator              must be inside a tuple and the default data type is float
a = np.zeros((3,3))
print(a)  # creates a matrix of 3x3 with zeros (float32)

a = np.ones((3,3))
print(a)  # creates a matrix of 3x3 with ones (float32)

a = np.full((3,3),5)
print(a) # creates a matrix of 3x3 with ones (int32)
print(a.dtype)

a = np.eye(3)  # it takes one argument only
print(a)       # it prints one in diagonal remaining zeros

ran = np.random.random((3,3))
print(ran)

ran = np.random.randint(1,10, size=(3,3))
print(ran)  # this will create a matrix of random integers of 3x3 matrix within 1 and 10

x = np.array([1,2,3,4,5])
ran = np.random.choice(x,size=(3,3))
print(ran)    # this takes only one parameter, so you can use an array


#  *** *** Loading text file *** ***
#data = np.loadtxt("error.txt",dtype=,delimiter="")
#data = np.genfromtxt("error.txt",dtype=,delimiter="")




























































