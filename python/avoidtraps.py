from sys import stdin,stdout
def seive(n):
    prime=[True]*(n+1)
    prime[0]=False
    prime[1]=False
    p=2
    while (p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    return(prime)
prime=seive(10**5)
x=[0]*((10**5)+1)
for i in range(1,(10**5)+1):
    if prime[i]==True:
        x[i]=x[i-1]+1
    else:
        x[i]=x[i-1]
ans=""
t=int(stdin.readline())
for i in range(t):
    r1,r2=map(int,stdin.readline().split())
    n=int(stdin.readline())
    a=[0]*(n+1)
    for i in range(1,n):
        u=x[i]/i
        v=r1/r2
        if u>=v:
            a[i]=x[i]
        else:
            a[i]=0
    dp=[(10**6)]*(n+1)
    s=stdin.readline()
    dp[1]=0
    for i in range(1,n):
        if s[i-1]=="#":
            if (i+1)<=n:
                dp[i+1]=min(dp[i+1],dp[i]+1)
            if (i+2)<=n:
                dp[i+2]=min(dp[i+2],dp[i]+1)
            if (i+a[i])<=n:
                dp[i+a[i]]=min(dp[i+a[i]],dp[i]+1)
    if dp[n]==(10**6) or s[n-1]=="*":
        ans+=("No way!"+'\n')
    else:
        ans+=(dp[n]+'\n')
print(ans)
