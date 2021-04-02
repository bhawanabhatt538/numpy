import pandas as pd
import numpy as np

# Arithmetic
# You can easily perform array with array arithmetic, or scalar with array arithmetic. Let's see some examples:
arr = np.arange(0,10)
print('sum=',arr + arr)
print('multification=',arr*arr)
print('arr-arr=',arr-arr)

# Warning on division by zero, but not an error!
# Just replaced with nan
print('arr/arr=',arr/arr)

# Also warning, but not an error instead infinity
print(1/arr)

print(arr**3)

print('\n\n')
# Universal Array Functions
# Numpy comes with many universal array functions, which are essentially just mathematical operations you can use to perform the operation across the array. Let's show some common ones:
#Taking Square Roots
print(np.sqrt(arr))
print('\n\n')
#Calcualting exponential (e^)
print(np.exp(arr))
print('\n\n')
print(np.max(arr))
print('\n')
print(np.min(arr))
print('\n')
print(np.sin(arr))
print('\n')
print(np.log(arr))
