#top down
''' dp=[[-1 for i in range(k+1)] for j in range(n+1)]
def bicoeff(n,k):
    if dp[n][k]!=-1:
        return(dp[n][k])
    else:
        if k==0 or k==n:
            dp[n][k]=1
        else:
            dp[n][k]=bicoeff((n-1),(k-1))+bicoeff(n-1,k)
        return(dp[n][k])'''
#bottom up
def bicoeff(n,k):
    dp=[[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if j==0 or j==n:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    return(dp[n][k])



