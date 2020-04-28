import math
def solve(l,k,d):
    for i in l:
        k=(math.ceil(k/i))*i
    return k<=d
t=int(input())
for z in range(1,t+1):
    n, d=map(int,input().split())
    l=list(map(int,input().split()))
    low=1
    high=d
    count=0
    while low<=high:
        mid=(low+high)//2
        if solve(l,mid,d)==True:
            if mid>count:
                count=mid
            low=mid+1
        else:
            high=mid-1
    print("Case #"+str(z)+": "+str(count))
