#bitonic
def lis(l):
    lis=[1]*len(l)
    n=len(l)
    for i in range(1,len(l)):
        for j in range(i):
            if l[i]>l[j]:
                lis[i]=max(lis[i],(lis[j]+1))
    dis=[1]*len(l)
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            if l[i]>l[j]:
                dis[i]=max(dis[i],(dis[j]+1))
    maxi=0
    for i in range(len(l)):
        if lis[i]+dis[i]>maxi:
            maxi=lis[i]+dis[i]
    return(maxi-1)
arr =  [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15] 
print(lis(arr))
