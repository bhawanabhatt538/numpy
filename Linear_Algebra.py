import numpy as np

print(np.__version__)

#MATRIX AND VECTOR PRODUCTS

#predict the result of the following code.

# x=[1,2]
# y=[[4,1],[2,2]]
# print(np.dot(x,y))
# print(np.dot(y,x))
# print(np.matmul(x,y))
# print(np.inner(x,y))
# print(np.inner(y,x))

# print('\n\n')
# #predict the results of the following code
# x = [[1,0],[0,1]]
# y = [[4,1],[2,2],[1,1]]

# print(np.dot(y,x))
# print(np.dot(y,x))


# #predict the results of the following code.
# print('\n\n')
# x = np.array([[1,4],[5,6]])
# y = np.array([[4,1],[2,2]])
# print(np.vdot(x,y))
# print(np.vdot(y,x))


# print('\n\n')



#Decompositions
##Q5. Get the lower-trianglular L in the Cholesky decomposition of x and verify it.


# Matrix eigenvalues
# Q8. Compute the eigenvalues and right eigenvectors of x. (Name them eigenvals and eigenvecs, respectively)



x = np.diag((1,2,3))
eigenvals,eigenvecs = np.linalg.eig(x)
print('eigen vals=',eigenvals,'\n\n','eigenvecs=','\n\n',eigenvecs)
#OR
print('eigenvals = {}\neigenvecs=\n{}'.format(eigenvals,eigenvecs))
