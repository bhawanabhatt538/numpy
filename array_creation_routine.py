import numpy as np
#Create a new array of 2*2 integers, without initializing entries.
print(np.zeros([2,2],int))
print(np.ones([3,3],int))

print('\n\n\n')

X = np.array([[1,2,3], [4,5,6]], np.int32)
print(np.empty_like(X))

print(np.eye(4))

print('\n\n\n')

print(np.identity(3))

print('\n\n')

print(np.ones([4,3]))

# Let x = np.arange(4, dtype=np.int64). Create an array of ones with the same shape and type as X.

x = np.arange(4, dtype=np.int64)
print('array of ones with the same shape and type as X',np.ones_like(x))

# Create a new array of 3*2 float numbers, filled with zeros.
print(np.zeros([3,2],float))

print('\n\n')
# Create a new array of 2*5 uints, filled with 6.
print(np.full([2,5],6))

print('\n\n')

#OR
print(np.ones([2,5], int)*6)

print('\n\n')

#From existing data:-

#create an array of [1,2,3]
print(np.arange(1,4))
print('\n\n')
#Let x = [1, 2]. Convert it into an array.

x= [1,2]
print(np.array(x))

print(np.asarray(x))

print('\n\n')


#Let X = np.array([[1, 2], [3, 4]]). Convert it into a matrix.
#
X = np.array([[1, 2], [3, 4]])
print(np.matrix(X))

print('\n\n')

X = [1,2]
print(np.asarray(X,float))

print(np.asfarray(X))

x=np.array([30])
print(np.asscalar(x))

print('\n\n')

#create a array copy of  x ,which has different id from id from x
x = np.array([1,2,3])
y = np.copy(x)
print(id(x),x)
print(id(y),y)


#Create an array of 2, 4, 6, 8, ..., 100.
print(np.arange(2,101,2))
#Create a 1-D array of 50 evenly spaced elements between 3. and 10., inclusive.
print(np.linspace(3,10,50))

print('\n\n')
#Create a 1-D array of 50 element spaced evenly on a log scale between 3. and 10., exclusive.
print(np.logspace(3,10,50,endpoint = False))

print('\n\n')

print(np.logspace(3,10,50))


#Building matrices
#Let X = np.array([[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]]). Get the diagonal of X, that is, [0, 5, 10].
print('\n\n')


X = np.array([[ 0, 1, 2, 3], [ 4, 5, 6, 7], [ 8, 9, 10, 11]])
print(np.diag(X))

print('\n\n')
#Create a 2-D array whose diagonal equals [1, 2, 3, 4] and 0's elsewhere.

print(np.diagflat([1,2,3,4]))


print('\n\n')
#Create an array which looks like below. array([[ 0, 0, 0], [ 4, 0, 0], [ 7, 8, 0], [10, 11, 12]])
print(np.tril(np.arange(1,13).reshape(4,3),-1))


print('\n\n')
#Create an array which looks like below. array([[ 1, 2, 3], [ 4, 5, 6], [ 0, 8, 9], [ 0, 0, 12]])
print(np.triu(np.arange(1,13).reshape(4,3),-1))


