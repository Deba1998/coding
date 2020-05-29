import math
def gcd(a,b): 
    if (b == 0): 
         return a 
    return gcd(b, a%b)
def primeFactors(n,m): 
    l=[]
    while n % 2 == 0: 
        l.append(2) 
        n = n // 2
    for i in range(3,min(m,int(math.sqrt(n))+1),2): 
        while n % i== 0: 
            l.append(i) 
            n = n //i 
    if n > 2: 
        if n<m:
            l.append(n)
    return(l)

t=int(input())
for i in range(t):
    x, y, m=map(int,input().split())
    destn=gcd(x,y)
    ans1=(x//destn)
    ans2=(y//destn)
    l1=primeFactors(ans1,m)
    l2=primeFactors(ans2,m)
    count1=1
    for i in range(len(l1)):
        count1=count1*l1[i]
    count2=1
    for i in l2:
        count2=count2*i
    if ans1==count1 and ans2==count2:
        print(len(l1)+len(l2),end=" ")
        print(destn)
    else:
        print(-1)
    