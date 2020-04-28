n=int(input())
l=list(map(int,input().split()))
g=[0]*n
g[0]=l[0]
for i in range(1,n):
    g[i]=g[i-1]+l[i]
g.insert(0,0)
o=l[:]
o.sort()
h=[0]*n
h[0]=o[0]
for i in range(1,n):
    h[i]=h[i-1]+o[i]
h.insert(0,0)
m=int(input())
for i in range(m):
    x, y, z=map(int,input().split())
    if x==1:
        print(g[z]-g[y-1])
    else:
        print(h[z]-h[y-1])

