# my method
'''def lps(s):
    n=len(s)
    t=s[::-1]
    dp=[[0 for i in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return(dp[n][n])'''
#bottom up
def lps(s):
    n=len(s)
    dp=[[0 for i in range(n)] for i in range(n)]
    for length in range(1,n+1):
        for i in range(n-length+1):
            j=(i+length)-1
            if i==j:
                dp[i][j]=1
            else:
                if s[i]==s[j] and length==2:
                    dp[i][j]=2
                elif s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
    return(dp[0][n-1])
print(lps("abbabba"))
                

