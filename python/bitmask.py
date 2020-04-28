t=int(input())
for z in range(1,t+1):
    n=int(input())
    l=[]
    for i in range(n):
        x, y=map(int,input().split())
        l.append((x,y))
    x=dict()
    for i in range(len(l)):
        if l[i] not in x:
            x[l[i]]=[i]
        else:
            x[l[i]].append(i)
    g=l[0:]
    k=[0]*n
    g.sort()
    Jmax=0
    flag=0
    k[x[g[0]][0]]="C"
    if len(x[g[0]])==2: 
        x[g[0]].remove(x[g[0]][0])
    Cmax=g[0][1]
    for i in range(1,n):
        if g[i][0]<Cmax:
            if g[i][0]<Jmax:
                s="IMPOSSIBLE"
                flag=1
                break
            else:
                k[x[g[i]][0]]="J"
                Jmax=g[i][1]
                if len(x[g[i]])==2:
                    x[g[i]].remove(x[g[i]][0])
        else:
            k[x[g[i]][0]]="C"
            Cmax=g[i][1]
            if len(x[g[i]])==2:
                    x[g[i]].remove(x[g[i]][0])
    if flag==0:
        s="".join(k)
        print("Case #"+str(z)+": "+s)
    else:
        print("Case #"+str(z)+": "+s)