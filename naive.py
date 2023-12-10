import pandas as pd
import numpy as np
# p(c|x)=p(x|c)*p(c)
# p(x|c)=p(x1|c)*p(x2|c)*......
df=pd.read_csv('C:/Users/Alan Shaiju/Python Codes/Data Analytics/dataset.csv')
feature1=df['feature1'].tolist()
feature2=df['feature2'].tolist()
feature3=df['feature3'].tolist()
feature4=df['feature4'].tolist()
label=df['label'].tolist()
no_yes=label.count(1)
no_no=label.count(0)
probability_yes=no_yes/len(label)
probability_no=no_no/len(label)
#get user data
print('Enter data to check:')
f1=int(input('Enter Feature1:'))
f2=int(input('Enter Feature2:'))
f3=int(input('Enter Feature3:'))
f4=int(input('Enter Feature4:'))
count_f1=0
count_f2=0
count_f3=0
count_f4=0
#compute for yes
for i in range(0,len(label)):
    if feature1[i]==f1 and label[i]==1:
        count_f1+=1
    if feature2[i]==f2 and label[i]==1:
        count_f2+=1
    if feature3[i]==f3 and label[i]==1:
        count_f3+=1
    if feature4[i]==f4 and label[i]==1:
        count_f4+=1
p_x_yes=(count_f1*count_f2*count_f3*count_f4)/((no_yes)**4)
count_f1=0
count_f2=0
count_f3=0
count_f4=0
#compute for no
for i in range(0,len(label)):
    if feature1[i]==f1 and label[i]==0:
        count_f1+=1
    if feature2[i]==f2 and label[i]==0:
        count_f2+=1
    if feature3[i]==f3 and label[i]==0:
        count_f3+=1
    if feature4[i]==f4 and label[i]==0:
        count_f4+=1
p_x_no=(count_f1*count_f2*count_f3*count_f4)/((no_no)**4)
p_yes_x=p_x_yes*probability_yes
p_no_x=p_x_no*probability_no
if p_yes_x>p_no_x:
    print("Predicted output is Yes")
else:
    print("Predicted output is No")