n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0 for i in range(n+1)]for i in range(3)]
for i in range(1,n+1):
    dp[0][i]=a[i-1]+max(dp[1][i-1],dp[2][i-1])
    dp[1][i]=b[i-1]+max(dp[0][i-1],dp[2][i-1])
    dp[2][i]=max(dp[0][i-1],dp[1][i-1])
print(max(dp[0][n],dp[1][n],dp[2][n]))
    

