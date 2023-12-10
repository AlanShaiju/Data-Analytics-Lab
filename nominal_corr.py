x=int(input('Enter the no. of attributes in the x axis'))
y=int(input('Enter the no. of attributes in the y axis'))
import numpy as np
matrix1=np.zeros((x,y))
vertical=[]
horizontal=[]
for i in range (0,x):
    horizontal.append(0)
sumv=0
sumh=0
for i in range (0,x):
    for j in range (0,y):
        print('Enter value for row ',i+1,' in column ',j+1,' :')
        z=int(input())
        matrix1[i][j]=z
        horizontal[j]=horizontal[j]+matrix1[i][j]
        sumh=sumh+matrix1[i][j]
    vertical.append(sumh)
    sumh=0
print(matrix1)
print(vertical)
print(horizontal)
expected=np.zeros((x,y))
for i in range(0,x):
    for j in range(0,y):
        expected[i][j]=vertical[i]*horizontal[j]/sum(vertical)
print(expected)
chi=0
print('Chi^2 ting')
for i in range (0,x):
    for j in range (0,y):
        chi=chi+(((matrix1[i][j]-expected[i][j])**2)/expected[i][j])
print(chi)