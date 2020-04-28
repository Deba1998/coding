t=int(input())
for z in range(1,t+1):
    n=int(input())
    l=[]
    for i in range(n):
        x, y=map(int,input().split())
        l.append((x,y))
    s="C"
    cmax=l[0][1]
    cmin=l[0][0]
    jmax=0
    jmin=0
    flag=0
    if len(l)>1:
        for i in range(1,n):
            if l[i][0]<cmax and l[i][0]>cmin:
                if l[i][0]<jmax:
                    v="IMPOSSIBLE"
                    flag=1
                    break
                else:
                    jmax=l[i][1]
                    s+="J"
            else:
                cmax=l[i][1]
                s+="C"
    if flag==0:
        print("Case #"+str(z)+": "+s)
    else:
        print("Case #"+str(z)+": "+v)

