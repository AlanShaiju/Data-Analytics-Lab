import numpy as np
import statistics
import pandas as pd
import math
mylist=[]
x=int(input('Whats the number of data objects:'))
print('Enter data:')
for i in range (0,x):
    y=int(input())
    mylist.append(y)
mylist.sort()
q1=mylist[math.floor(len(mylist)*0.25)]
print('q1 is:',q1)
q3=mylist[math.floor(len(mylist)*0.75)]
print('q1 is:',q3)
iqr=q3-q1
print('IQR:',iqr)
outliers=[]
for i in mylist:
    if i not in range((q1-iqr*1.5),(q3+iqr*1.5)):
        outliers.append(i)
print('Outliers:',outliers)
print('Mean:',np.mean(mylist))
print('Median:',np.median(mylist))
print('Mode:',statistics.mode(mylist))
print('Mode:',statistics.mode(mylist))
df=pd.DataFrame(mylist,columns=['marks'])
no_modes=df.mode().count()
if no_modes==1:
    print('Unimodal')
elif no_modes==2:
    print('Bimodal')
else:
    print('Trimodal')