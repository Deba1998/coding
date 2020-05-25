import math
def issquare(n):
    r=math.sqrt(n)
    return((r-math.floor(r))==0)
t=int(input())
for z in range(1,t+1):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    pref=[0]
    com=0
    for i in range(n):
        com+=l[i]
        pref.append(com)
    for i in range(0,n):
        for j in range(i+1,n+1):
            if issquare(pref[j]-pref[i]):
                count+=1
    print("Case #"+str(z)+": "+str(count))