t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    l.sort()
    r.sort()
    i=0
    j=0
    count=0
    while i<n and j<n:
        if l[i]<=r[j]:
            i+=1
        else:
            count+=1
            i+=1
            j+=1
    print(count)