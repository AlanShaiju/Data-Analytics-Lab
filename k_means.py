import numpy as np
points=[]
def euc(a,b):
    return((sum((x-y)**2 for x,y in zip(a,b)))**0.5)
n=int(input('Enter number pof data points:'))
for i in range (0,n):
    print('Enter data point ',i+1,':')
    x=list(map(float,input().split()))
    points.append(x)
print(points)
print(np.mean(points,axis=0))
k=int(input('Enter no. of clusters:'))
clusters=[0]*n
centroids=[0]*k
new_centroids=[0]*k
clusterset=[]
centroids=points[:k]
print(centroids)
matrix1=np.zeros((n,k))
for _ in range (0,100):
    for i in range (0,n):
        for j in range (0,k):
            matrix1[i][j]=euc(points[i],centroids[j])
        mincol=np.argmin(matrix1[i])
        clusters[i]=mincol
    print('Clusters in iteration:',_+1)
    for m in range (0,k):
        for i in range (0,n):
            if clusters[i]==m:
                clusterset.append(points[i])
        new_centroids[m]=np.mean(clusterset,axis=0)
        print('Cluster ',m+1,' elements:',clusterset)
        clusterset=[]
        
    if np.array_equal(new_centroids,centroids):
        break
    else:
        centroids=new_centroids
print('Final Centroids:',centroids)
print('Final Clusters:')
for m in range (0,k):
   for i in range (0,n):
       if clusters[i]==m:
           clusterset.append(points[i])
   print('Cluster ',m+1,' elements:',clusterset)
   clusterset=[]     