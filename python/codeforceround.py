import math
for  i in range(int(input())):
    s=input()
    m=int(input())
    l=list(map(int,input().split()))
    if m==len(s):
        print(s)
    elif m==1 and l[0]==0:
        print(s[0])
    else:
        g=l[:]
        g.sort()
        index=[]
        for i in g:
            index.append


 