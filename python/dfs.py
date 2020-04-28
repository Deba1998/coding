def dfsut(l,v,pk,b):
    pk[v]=True
    for i in l[v]:
        if pk[i]==False:
            if b[i]==0:
                dfsut(l,i,pk,b)
    return(pk)
n, k=map(int,input().split())
ly=[False]*n
l=[[]for i in range(n)]
for i in range(n-1):
    x, y=map(int,input().split())
    l[x-1].append(y-1)
j=list(map(int,input().split()))
b=[0]*n
for i in j:
    b[i-1]=1

hgf=dfsut(l,0,ly,b)
print(hgf.count(True)-1)


