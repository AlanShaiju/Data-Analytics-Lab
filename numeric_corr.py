import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Alan Shaiju/Python Codes/Data Analytics/data1.csv')
print(df)
list1=df['attribute1'].tolist()
list2=df['attribute2'].tolist()
covariance=0
mean_list1=np.mean(list1)
print(mean_list1)
mean_list2=np.mean(list2)
print(mean_list2)
for i in range(0,len(list1)):
    covariance+=((list1[i]-mean_list1)*(list2[i]-mean_list2))
print(covariance)
covariance=covariance/len(list1)
print('Covariance:',covariance)
print('Correlation:',covariance/(np.std(list1)*np.std(list2)))