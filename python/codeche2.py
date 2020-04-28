import math
def check(n):
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if i%2==0:
                if (n//i)%2==0:
                    return(1)
            else:
                if (n//i)%2!=0:
                    return(1)
    return(0)
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    fu=[0]*len(l)
    oo=1
    sum=0
    for i in range(n):
        if l[i]%2==0:
            fu[i]=1
        else:
            fu[i]=0
    for i in range(1,n):
        if fu[i]==fu[i-1]:
            oo+=1
        else:
            sum+=((oo)*(oo+1)//2)
            oo=1
    sum+=(oo*(oo+1)//2)
    sum-=n
    for i in range(n):
        if check(l[i])==1:
            sum+=1
    print(sum)


