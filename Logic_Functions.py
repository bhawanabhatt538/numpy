import numpy as np


#Q3= predict the result of the following code

x = np.array([1, 0, np.nan, np.inf ])
print(np.isfinite(x))

print('\n\n')
x = np.array([1, 0, np.nan, np.inf])
print(np.isinf(x))

print('\n\n')

x = np.array([1, 0, np.nan, np.inf])
print(np.isnan(x))

print('\n\n')
x= np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print(np.iscomplex(x))

print('\n\n')
x= np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print(np.isreal(x))

print('\n\n')
print(np.isscalar(3))
print(np.isscalar([3]))
print(np.isscalar(True))

print('\n\n')
#LOGICAL OPRATIONS

print(np.logical_and([True, False],[False, False]))

print(np.logical_or([True, False,True],[True,False, False]))

print(np.logical_xor([True, False, True],[True, False, False]))

print(np.logical_not([True, False, 0, 1]))

print('\n\n')
#COMPERISION

print('array close=',np.allclose([3], [2.999999]))

print('array equal=',np.array_equal([3],[2.999999]))

x = np.array([4,5])
y = np.array([2,5])
print(np.array_equal([5],[5]),([4]))




