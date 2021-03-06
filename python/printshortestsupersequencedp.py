#bottom up
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
    return(dp)
s="abcde"
m=len(s)
t="ablcgfe"
n=len(t)
li=lcs(s,t)
j=n
i=m
ans=""
while i>0 and j>0:
    if s[i-1]==t[j-1]:
        ans+=s[i-1]
        i-=1
        j-=1
    else:
        if li[i][j-1]>li[i-1][j]:
            ans+=t[j-1]
            j-=1
        else:
            ans+=s[i-1]
            i-=1
while i>0:
    ans+=s[i-1]
    i-=1
while j>0:
    ans+=t[j-1]
    j-=1
print(ans[::-1])