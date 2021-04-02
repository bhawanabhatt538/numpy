import numpy as np

# # calculate sinne , cosine and tangent of x,element-wise

# # Trigonometric functions
# # Q1. Calculate sine, cosine, and tangent of x, element-wise.

# # In [8]:
# x = np.array([0., 1., 30, 90])
# print("sine: {} \ncosine: {} \ntangent: {}".format(np.sin(x),np.cos(x),np.tan(x)))

# print('\n\n')
# # Q2. Calculate inverse sine, inverse cosine, and inverse tangent of x, element-wise.

# # In [14]:
# x = np.array([-1., 0, 1.])
# print("sine: {} \ncosine: {} \ntangent: {}".format(np.arcsin(x),np.arccos(x),np.arctan(x)))

# print('\n\n')
# # Q3. Convert angles from radians to degrees.

# # In [19]:
# x = np.array([-np.pi, -np.pi/2, np.pi/2, np.pi])
# deg = np.degrees(x)
# print(deg)

# print('\n\n')
# # Q4. Convert angles from degrees to radians.

# x = np.array([-180.,  -90.,   90.,  180.])
# print(np.deg2rad(x))

# #Hyperbolic functions
# # Q5. Calculate hyperbolic sine, hyperbolic cosine, and hyperbolic tangent of x, element-wise.
# x = np.array([-1., 0, 1.])
# print(np.sinh(x))
# print(np.cosh(x))
# print(np.tanh(x))
# #OR
# print('\n\n')
# print('sine:{}\n cosine:{}\n tangent:{}'.format(np.sinh(x),np.cosh(x),np.tanh(x)))

# print('\n\n')
# # Rounding
# # Q6. Predict the results of these, paying attention to the difference among the family functions.
# x = np.array([2.1, 1.5, 2.5, 2.9, -2.1, -2.5, -2.9])
# c1 = np.around(x)
# c2 = np.floor(x)
# c3 = np.ceil(x)
# c4 = np.trunc(x)
# c5 = np.round(x)

# out5 = [round(elem) for elem in x]

# print(c1)
# print(c2)
# print(c3)
# print(c4)
# print(c5)
# print(out5)

# Sums, products, differences
# Q8. Predict the results of these.
# x = np.array(
#     [[1, 2, 3, 4],
#      [5, 6, 7, 8]])

# out = [np.sum(x),
#        np.sum(x,axis=0),
#        np.sum(x,axis=1,keepdims=True),
#        "",
#        np.prod(x),
#        np.prod(x,axis=0),
#        np.prod(x,axis=1,keepdims=True),
#        "",
#        np.cumsum(x),
#        np.cumsum(x, axis=0),
#        np.cumsum(x, axis=1),
#        "",
#        np.min(x),
#        np.min(x,axis=0),
#        np.min(x,axis=1,keepdims=True),
#        "",
#        np.max(x),
#        np.max(x,axis=0),
#        np.max(x,axis=1,keepdims=True),
#        "",
#        np.mean(x),
#        np.mean(x,axis=0),
#        np.mean(x,axis=1,keepdims=True)]

# for i in out:
#     if i=="":
#         pass
#         print

#     else:
#         pass
#         print("->",out)

# #OR
# print(out)

# print('\n\n')

# # Q9. Calculate the difference between neighboring elements, element-wise.

# # In [29]:
# x = np.array([1, 2, 4, 7, 0])
# print(np.diff(x))

# print('\n\n')
# x = np.array([1,2,3,4,7,0])
# print(np.ediff1d(x, to_begin=[0,0],to_end=[100]))

# print('\n\n')

# #Return the cross product of x and y
# x = np.array([1,2,3])
# y = np.array([4,5,6])
# z = np.cross(x,y)
# print(z)

# print('\n\n')
# # Exponents and logarithms
# # Q12. Compute $e^x$, element-wise.
# x = np.array([1., 2., 3.], np.float32)
# print(np.exp(x))
# print('\n\n')

# # Q13. Calculate exp(x) - 1 for all elements in x.

# # In [41]:
# x = np.array([1., 2., 3.], np.float32)
# print(np.exp(x)-1)
# print('\n\n')

# # Q14. Calculate $2^p$ for all p in x.

# # In [46]:
# x = np.array([1., 2., 3.], np.float32)
# print(2**x)
# out =  np.exp2(x)
# print(out)

# # Q15. Compute natural, base 10, and base 2 logarithms of x element-wise.

# # In [50]:
# x = np.array([1, np.e, np.e**2])
# print('natural log ={}'.format(np.log(x)))
# print('common log = {}'.format(np.log10(x)))
# print('base 2 log = {}'.format(np.log2(x)))

# print('\n\n')
# # Q16. Compute the natural logarithm of one plus each element in x in floating-point accuracy.

# # In [63]:
# x = np.array([1e-99, 1e-100])
# print(np.log1p(x))
# print('\n\n')

# # Floating point routines
# # Q17. Return element-wise True where signbit is set.

# # In [65]:

# x = np.array([-3, -2, -1, 0, 1, 2, 3])
# print(np.signbit(x))
# print('\n\n')


# # Q18. Change the sign of x to that of y, element-wise.
# x = np.array([-1, 0, 1])
# y = -1.1
# print(np.copysign(x,y))

# Arithmetic operations
# Q19. Add x and y element-wise.

# In [81]:
x = np.array([1, 2, 3])
y = np.array([-1, -2, -3])
print('Add x and y element-wise=',x+y)
print('Add x and y element-wise=',np.add(x,y))

print('\n\n')
# Q20. Subtract y from x element-wise.

# In [83]:
x = np.array([3, 4, 5])
y = np.array(3)
print(' Subtract y from x element-wise=',np.subtract(x,y))

print('\n\n')
# Q21. Multiply x by y element-wise.

# In [86]:
x = np.array([3, 4, 5])
y = np.array([1, 0, -1])
print('Multiply x by y element-wise=',np.multiply(x,y))


# Q22. Divide x by y element-wise in two different ways.

# In [103]:
x = np.array([3., 4., 5.])
y = np.array([1., 2., 3.])
print(' Divide x by y element-wise=',np.divide(x,y))
print('Divide x by y element-wise=', np.true_divide(x,y))
print(' Divide x by y element-wise=',np.floor_divide(x,y))

print('\n\n')

# Q23. Compute numerical negative value of x, element-wise.

x = np.array([1, -1])
print('Compute numerical negative value of x=',np.negative(x))


# Q24. Compute the reciprocal of x, element-wise.

# In [106]:
x = np.array([1., 2., .2])
print('Compute the reciprocal of x=',np.reciprocal(x))


# Q25. Compute $x^y$, element-wise.

# In [109]:
x = np.array([[1, 2], [3, 4]])
y = np.array([[1, 2], [1, 2]])
print(x**y)
print(np.power(x,y))

print('\n\n')
# Q26. Compute the remainder of x / y element-wise in two different ways.

# In [118]:
x = np.array([-3, -2, -1, 1, 2, 3])
y = 2
print('Compute the remainder of x / y element-wise=',np.remainder(x,y))
print('Compute the remainder of x / y element-wise=',np.fmod(x,y))


print('\n\n')
# Miscellaneous
# Q27. If an element of x is smaller than 3, replace it with 3. And if an element of x is bigger than 7, replace it with 7.
x = np.arange(10)
print(np.clip(x,3,7))


# Q28. Compute the square of x, element-wise.

# In [122]:
x = np.array([1, 2, -1])
print('Compute the square of x=',np.square(x))

# Q29. Compute square root of x element-wise.

# In [123]:
x = np.array([1., 4., 9.])
print('Compute square root of x element-wise=',np.sqrt(x))

#Q30. Compute the absolute value of x.
x = np.array([[1, -1], [3, -3]])
print('Compute square root of x element-wise=',np.abs(x))

# Q31. Compute an element-wise indication of the sign of x, element-wise.

# In [125]:
x = np.array([1, 3, 0, -1, -3])
print('Compute an element-wise indication of the sign of x=',np.sign(x))

