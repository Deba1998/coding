import math
t=int(input())
for i in range(t):
    n=int(input())
    a,b,c=map(int,input().split())
    u=input()
    l=[]
    for i in u:
        l.append(i)
    x=[0,0,0]
    for i in l:
        if i=="R":
            x[0]+=1
        if i=="S":
            x[1]+=1
        if i=="P":
            x[2]+=1
    count=0
    count+=min(x[1],a)
    count+=min(x[0],b)
    count+=min(x[2],c)
    if count>=(math.ceil(n/2)):
        print("YES")
        o=[]
        for i in range(n):
            if l[i]=="R":
                if b>0:
                    o.append("P")
                    b-=1
                else:
                    o.append(0)
            if l[i]=="S":
                if a>0:
                    o.append("R")
                    a-=1
                else:
                    o.append(0)
            if l[i]=="P":
                if c>0:
                    o.append("S")
                    c-=1
                else:
                    o.append(0)
        for i in range(n):
            if o[i]==0:
                if a>0:
                    o[i]="R"
                    a-=1
                elif b>0:
                    o[i]="P"
                    b-=1
                else:
                    o[i]="S"
        print("".join(o))
    else:
        print("NO")
    
