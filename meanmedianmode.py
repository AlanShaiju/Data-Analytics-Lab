import numpy as np
r=[]
i=int(input('Enter no of elements to store to list'))
for j in range (0,i):
    x=int(input('Enter element:'))
    r.append(x)
print('Mean:',np.mean(r))
print('Median:',np.median(r))
import statistics
print('Mode:',statistics.mode(r))