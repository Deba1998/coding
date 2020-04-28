import sys
ans=""
for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    a=[]
    b=[]
    for i in range(n):
        x, y=map(int, sys.stdin.readline().split())
        a.append(x)
        b.append(y)
    h=[0]*n
    h[0]=max(0,(a[0]-b[n-1]))
    for i in range(1,n):
        h[i]=max(0,(a[i]-b[i-1]))
    fd=sum(h)
    maxi=a[0]+(fd-h[0])
    for i in range(1,n):
        if a[i]+(fd-h[i])<maxi:
            maxi=a[i]+(fd-h[i])
    ans+=str(maxi)+"\n"
print(ans)
