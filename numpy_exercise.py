import pandas as pd
import numpy as np
# Create an array of 10 zeros
print('array of 10 zeros=',np.zeros(10))

print('array of 10 ones=',np.ones(10))

#Create an array of 10 fives
print('an array of 10 fives=',np.ones(10)*5)

print('array of the integers from 10 to 50=',np.arange(10,51))
print('array of all the even integers from 10 to 50=',
np.arange(10,51,2))

print(np.arange(0,9).reshape([3,3]))

print('3x3 identity matrix=\n',np.eye(3))

# Use NumPy to generate a random number between 0 and 1
print(np.random.rand(1))

print('\n')

print('an array of 25 random numbers sampled from a standard normal distribution=',np.random.randn(25))

# print(np.arange(0.01,0,01,0.01).reshape(10,10))

# print('array of 20 linearly spaced points between 0 and 1=',np.linspace(0,1,20))

# Numpy Indexing and Selection
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
# Deepak = np.arange(1,26).reshape(5,5)
# print(Deepak)
print('\n\n')
mat = np.arange(1,26).reshape(5,5)
print(mat)

print('\n')
print(mat[2:,1:])

print('\n\n')
print(mat[3,4])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print('\n')
print(mat[:3,1:2])


print('\n')
print(mat[3:,:])

# print('\n\n')
# Now do the following
# Get the sum of all the values in mat¶
# print('sum of all the values in mat=',mat.sum())

print('standard deviation of the values in mat=',np.std(mat))
print('\n')

print('sum of all the columns in mat=',np.sum(mat,axis=0))
