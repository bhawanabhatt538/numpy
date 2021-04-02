import numpy as np

# Creating NumPy Arrays
# From a Python List
# We can create an array by directly converting a list or list of lists:
my_list = [1,2,3]
print(my_list)

print(np.array(my_list))

print('\n\n')
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)

print(np.array(my_matrix))

# Built-in Methods
# There are lots of built-in ways to generate Arrays

print('\n')
# arange
# Return evenly spaced values within a given interval

print(np.arange(10))
print(np.arange(0,11,2))

#zeros and ones
# Generate arrays of zeros or ones

print('arrays of zeros or ones=',np.zeros(2))
print(np.zeros((5,5)))

print('\n\n')
print(np.ones(3))
print(np.ones((3,3)))

print('\n\n')

# linspace
# Return evenly spaced numbers over a specified interval.

print(np.linspace(0,10,3))
print('\n\n')
print(np.linspace(0,10,50))

print('\n\n')
# eye
# Creates an identity matrix
print(np.eye(4))


# Random
# Numpy also has lots of ways to create random number arrays:

print('\n\n')
# rand
# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

print(np.random.rand(2))

print(np.random.rand(5,5))

# randint
# Return random integers from low (inclusive) to high (exclusive).
print(np.random.randint(1,100))
print(np.random.randint(1,100,10))

# Array Attributes and Methods
# Let's discuss some useful attributes and methods or an array:

print('\n\n')
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)

# Reshape
# Returns an array containing the same data with a new shape
print(arr.reshape(5,5))
print('\n\n')

# max,min,argmax,argmin
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax
print(ranarr)
print(ranarr)
print(ranarr.argmax())
print(ranarr.argmin())
print(ranarr.min())
print(ranarr.max())

# Shape
# Shape is an attribute that arrays have (not a method):

# In [65]:
# # Vector
print(arr.shape)

print('\n\n')
# Notice the two sets of brackets

print(arr.reshape(1,25))

print('\n\n')
print(arr.reshape(1,25).shape)

print('\n')
print(arr.reshape(25,1))

print('\n\n')
print(arr.dtype)
