n=int(input())
k=int(input())
a=int(input())
b=int(input())
dp=dict()
dp[n]=0
for i in range(n-1,0,-1):
    if (i*k)<=n:
        dp[i]=min(dp[i*k]+b,dp[i+1]+a)
    else:
        dp[i]=dp[i+1]+a
print(dp[1])
