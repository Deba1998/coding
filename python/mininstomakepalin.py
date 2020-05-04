def lps(s):
    n=len(s)
    t=s[::-1]
    dp=[[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return(dp[n][n])
s="abc"
print(len(s)-lps(s))
#minimum number of insertions and deletions to make a string palindrome
