def dis_numeric(x,y,maximum,minimum):
    return(abs(x-y)/(maximum-minimum))
def dis_nominal(str1,str2):
    if str1==str2:
        return 0
    else:
        return 1
import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/Alan Shaiju/Python Codes/Data Analytics/data.csv')
nominal=df['Nominal'].tolist()
numeric=df['Numeric'].tolist()
print(df)
print(nominal)
print(numeric)
x=len(nominal)
#print(x)
maximum=max(numeric)
minimum=min(numeric)
matrix1=np.zeros((x,x))
matrix2=np.zeros((x,x))
matrix3=np.zeros((x,x))
print(matrix1)
for i in range(0,x):
    for j in range (0,x):
        matrix1[i][j]=dis_numeric(numeric[i],numeric[j],maximum,minimum)
        matrix2[i][j]=dis_nominal(nominal[i],nominal[j])
        matrix3[i][j]=(matrix1[i][j]+matrix2[i][j])/2
print('Numeric Attributes')
print(matrix1)
print('Nominal')
print(matrix2)
print('Combined')
print(matrix3)