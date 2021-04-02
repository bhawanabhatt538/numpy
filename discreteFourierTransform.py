from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

from datetime import date
print('today date:',date.today())

author = "kyubyong. https://github.com/Kyubyong/numpy_exercises"

print(np.__version__)

#COMPLEX NUMBERS

# Q1. Return the angle of a in radian.
a=1+1j
output= np.angle(a)
print(output)


print('\n\n')
#Q2. Return the real part and imaginary part of a.
a=np.array([1+2j, 3+4j, 5+6j])
real=np.real(a)
imag=np.imag(a)
print('real_part=',real,'\n','imag_part=',imag)

#Q3. Replace the real part of a with 9, the imaginary part with [5, 7, 9].
print('\n\n')
a=np.array([1+2j, 3+4j, 5+6j])
a.real=9
a.imag=[5,6,7]
print(a)


#Q4. Return the complex conjugate of a.Q4. Return the complex conjugate of a.
a=1+2j
output= a.conjugate()
print('complex conjugate of a.=',output)

#Discrete Fourier Transform
#Q5. Compuete the one-dimensional DFT of a.

a=np.exp(2j*np.pi*np.arange(8))
output = np.fft()
print(output)

a=np.exp(2j*np.pi*













