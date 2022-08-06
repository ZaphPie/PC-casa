import numpy
A=[[4,3,4],[3,1,3],[3,3,2]]
B=[[7,8,8],[0,5,1],[0,6,0]]
C=numpy.zeros((3,3))
for i in range(3):
    for j in range(3):
        C[i][j]=A[i][j]*B[i][j]
print(C)