t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    x=dict()
    j=[0]*len(l)
    x[l[0]]=1
    for i in range(1,len(l)):
        count=-1
        for k in x:
            if k<l[i]:
                if k>count:
                    count=k
        x[l[i]]=1
        j[i]=count
    y=dict()
    p=[0]*len(l)
    y[l[n-1]]=1
    for ji in range(n-2,-1,-1):
        count1=-1
        for g in y:
            if g>l[ji]:
                if g>count1:
                    count1=g
        y[l[ji]]=1
        p[ji]=count1
    max=-1
    rti=-1
    for i in range(1,n-1):
        if j[i]!=-1 and p[i]!=-1:
            rti=j[i]+(l[i]*p[i])
        if rti>max:
            max=rti
    print(max)


