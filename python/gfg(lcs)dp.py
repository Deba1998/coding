'''#lcs boottommm up
def lcs(s,t):
    m=len(s)
    n=len(t)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return(dp[m][n])'''
#top down
def lcs(s,t,n,m):
    if m==0 or n==0:
        return 0
    if dp[n][m]!=-1:
        return(dp[n][m])
    if s[n-1]==t[m-1]:
        dp[n][m]=1+lcs(s,t,n-1,m-1)
        return(dp[n][m])
    else:
        dp[n][m]=max(lcs(s,t,n,m-1),lcs(s,t,n-1,m))
        return(dp[n][m])
s="abcde"
t="ablcgfe"
n=len(s)
m=len(t)
dp=[[-1 for i in range(m+1)] for i in range(n+1)]
print(lcs(s,t,n,m))