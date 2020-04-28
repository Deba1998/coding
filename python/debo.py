t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0
    for i in range(n):
        if l[i]<0:
            flag=1
            break
    if flag==0:
        print("YES")
    else:
        ds=[0]*n
        ds[0]=l[0]
        for i in range(1,n):
            ds[i]=max((ds[i-1]+l[i]),l[i])
        if max(ds)>=(sum(l)):
            print("NO")
        else:
            print("YES")