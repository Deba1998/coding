t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    for i in range(n):
        for j in range(n):
            sum=l[i]+l[j]
            v=max(i,j)
            x=l[v:]
            if sum in x:
                count+=1
    print(count)
