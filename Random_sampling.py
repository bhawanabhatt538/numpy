# Random Sampling¶
import numpy as np
print(np.__version__)

__author__ = 'kyubyong. longinglove@nate.com'
print('\n\n')
# Simple random data
# Q1. Create an array of shape (3, 2) and populate it with random samples from a uniform distribution over [0, 1).
print(np.random.rand(3,2))

print()
#Q2. Create an array of shape (1000, 1000) and populate it with random samples from a standard normal distribution. And verify that the mean and standard deviation is close enough to 0 and 1 repectively.
x = np.random.standard_normal(size=(1000,1000))
print(np.mean(x))
print(np.std(x))

print('\n\n')
#Q3. Create an array of shape (3, 2) and populate it with random integers ranging from 0 to 3 (inclusive) from a discrete uniform distribution.
print(np.random.randint(0,4,size=(3,2)))


#Q4. Extract 1 elements from x randomly such that each of them would be associated with probabilities .3, .5, .2. Then print the result 10 times.
x=[b'3 out of 10', b'5 out of 10', b'2 out of 10']
for i in range(10):
    print(np.random.choice(x,p=[0.3, 0.5,0.2]))

print('\n\n')
#Q5. Extract 3 different integers from 0 to 9 randomly with the same probabilities.
print(np.random.choice(range(10),size=3))


# Permutations
# Q6. Shuffle numbers between 0 and 9 (inclusive).

x = np.arange(10)
np.random.shuffle(x)
print('Shuffle numbers between 0 and 9=',x)

print('\n\n')
# Random generator
# Q7. Assign number 10 to the seed of the random generator so that you can get the same value next time.
print(np.random.seed(1))
print(np.random.rand(2))
