from __future__ import print_function
import numpy as np
author = "kyubyong. https://github.com/Kyubyong/numpy_exercises"

print(np.__version__)

#Q1. Concatenate x1 and x2.
x1 = np.array(['hello','say'])
x2 = np.array(['world','something'])
print(np.char.add(x1,x2))

# x = np.array(['Hello ', 'Say '], dtype=np.str)
# print(np.char.multiply())


x = np.array(['heLLo woRLd', 'Say sOmething'], dtype=np.str)
print('capitalized=',np.char.capitalize(x))
print('lowered=',np.char.lower(x))
print('uppered=',np.char.upper(x))
print('swapcase=',np.char.swapcase(x))
print('titlecae=',np.char.title(x))

x = np.array(['hello world', 'say something'], dtype=np.str)
centered = np.char.center(x,20,'_')
print(centered)
left = np.char.ljust(x,20,'_')
print(left)
right = np.char.rjust(x,20,'_')
print(right)

print('\n\n')
# Q5. Encode x in cp500 and decode it again.

# In [54]:
x = np.array(['hello world', 'say something'], dtype=np.str)
encoded = np.char.encode(x,'cp500')
print(encoded)
decode = np.char.decode(encoded , 'cp500')
print(decode)

# Q6. Insert a space between characters of x.
print('\n')
# In [61]:
x = np.array(['hello world', 'say something'], dtype=np.str)
print(np.char.join(' ',x))

# ]\Q7-1. Remove the leading and trailing whitespaces of x element-wise.
# Q7-2. Remove the leading whitespaces of x element-wise.
# Q7-3. Remove the trailing whitespaces of x element-wise.
print('\n')
x = np.array(['   hello world   ', '\tsay something\n'], dtype=np.str)
stripped = np.char.strip(x)
lstripped = np.char.lstrip(x)
rstripped = np.char.rstrip(x)
print("stripped =", stripped)
print("lstripped =", lstripped)
print("rstripped =", rstripped)

# Q8. Split the element of x with spaces.

# In [11]:
x = np.array(['Hello my name is John'], dtype=np.str)
print(x)
x = np.array(['Hello\nmy name is John'], dtype=np.str)
print(np.char.splitlines(x))

# Q10. Make x a numeric string of 4 digits with zeros on its left.

# In [44]:
x = np.array(['34'], dtype=np.str)
print(np.char.ljust(x,4,'0'))

# Q11. Replace "John" with "Jim" in x.

# In [40]:
x = np.array(['Hello nmy name is John'], dtype=np.str)
print('{}'.format(np.char.replace(x,'John','Jim')))

# Q12. Return x1 == x2, element-wise.

# In [37]:
x1 = np.array(['Hello', 'my', 'name', 'is', 'John'], dtype=np.str)
x2 = np.array(['Hello', 'my', 'name', 'is', 'Jim'], dtype=np.str)
print(np.char.equal(x1,x2))

# Q13. Return x1 != x2, element-wise.

# In [38]:
x1 = np.array(['Hello', 'my', 'name', 'is', 'John'], dtype=np.str)
x2 = np.array(['Hello', 'my', 'name', 'is', 'Jim'], dtype=np.str)
print(np.char.not_equal(x1,x2))

# String information
# Q14. Count the number of "l" in x, element-wise.

# In [32]:
x = np.array(['Hello', 'my', 'name', 'is', 'Lily'], dtype=np.str)
print(np.char.count(x,'l'))

# Q16-1. Check if each element of x is composed of digits only.
# Q16-2. Check if each element of x is composed of lower case letters only.
# Q16-3. Check if each element of x is composed of upper case letters only
x = np.array(['Hello', 'I', 'am', '20', 'years', 'old'], dtype=np.str)
print("Digits only =",np.char.isdigit(x))
print("Lower cases only =", np.char.islower(x))
print("Upper cases only =", np.char.isupper(x))

# Q17. Check if each element of x starts with "hi".

# In [27]:
x = np.array(['he', 'his', 'him', 'his'], dtype=np.str)
print(np.char.startswith(x,'hi'))
