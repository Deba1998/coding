'''#bottom up
def lcs(s,t):
    m=len(s)
    n=len(t)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    maxi=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>maxi:
                    maxi=dp[i][j]
            else:
                dp[i][j]=0
    return maxi
a="abcwetrygf"
b="wetryabc"
print(lcs(a,b))'''
'''#top down 1
def lcs(s,t,n,m,count) :        
    if (n== 0 or m == 0) :
        dp[n][m] = 0
        return count  
    if dp[n][m]!=-1:
        return max(count, dp[n][m])   
    if (s[n- 1] == t[m - 1]) : 
        count = lcs(s,t,n- 1, m - 1, count + 1)
        dp[n][m] = 1 + dp[n-1][m-1]  
    else:
        dp[n][m] = 0
        count = max(lcs(s,t,n,m - 1, 0), lcs(s,t, n- 1, m, 0))
    return max(dp[n][m],count)
      
s="aaa"
t="aa"
n=len(s)
m=len(t)
dp=[[-1 for i in range(m+1)] for i in range(n+1)]
count = lcs(s,t,n,m,0)
print(count)'''
#top down2
def lcs(s,t,n,m,mx):
    if m==0 or n==0:
        dp[n][m]=0
        mx[0]=max(mx[0],dp[n][m])
    if dp[n][m]!=-1:
        mx[0]=max(mx[0],dp[n][m])
        return
    if s[n-1]==t[m-1]:
        lcs(s,t,n-1,m-1,mx)
        dp[n][m]=1+dp[n-1][m-1]
        mx[0]=max(dp[n][m],mx[0])
    else:
        dp[n][m]=0
        lcs(s,t,n,m-1,mx)
        lcs(s,t,n-1,m,mx)
        mx[0]=max(mx[0],dp[n][m])
      
s="abcde"
t="abcgfe"
n=len(s)
m=len(t)
dp=[[-1 for i in range(m+1)] for i in range(n+1)]
mx = [0]
lcs(s,t,n,m,mx)
print(mx[0])