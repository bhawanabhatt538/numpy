import pandas as pd
import numpy as np

arr = np.arange(0,11)
print(arr)


# Bracket Indexing and Selection
# The simplest way to pick one or some elements of an array looks very similar to python lists:

print(arr[8])
print(arr[1:5])
print(arr[0:5])

print('\n\n')
# arr[0:5]=100
# print(arr)

slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:]=99
print(slice_of_arr)

print('\n')
print(arr)

print('\n\n')
arr_copy = arr.copy()
print(arr_copy)

# Indexing a 2D array (matrices)
# The general format is arr_2d[row][col] or arr_2d[row,col]. I recommend usually using the comma notation for clarity.

# In [14]:

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

print('\n')
print(arr_2d[1])
print(arr_2d[1][0])
print(arr_2d[1,0])

# 2D array slicing

#Shape (2,2) from top right corner
print(arr_2d[:2,1:])

print(arr_2d[2])
#Shape bottom row
print('Shape bottom row=',arr_2d[2,:])

#Fancy Indexing
#Fancy indexing allows you to select entire rows or columns out of order,to show this, let's quickly build out a numpy array:

#Set up matrix
arr2d = np.zeros((10,10))
#Length of array
arr_length = arr2d.shape[1]
#Set up array
for i in range(arr_length):
    arr2d[i] = i
print('\n\n')
print(arr2d)

print('\n\n')
print(arr2d[[2,4,6,8]])
print('\n\n')

print('\n\n')
print(arr2d[[6,4,2,7]])

print('\n\n')
# More Indexing Help
# Indexing a 2d matrix can be a bit confusing at first, especially when you start to add in step size. Try google image searching NumPy indexing to fins useful images, like this one:
arr = np.arange(1,11)
print(arr)
print(arr>4)

bool_arr = arr>4
print(bool_arr)

print(arr[bool_arr])
print('\n')
print(arr[arr>2])
print('\n')
x=2
print(arr[arr>x])
