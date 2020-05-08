def ispalindrome(s,i,j):
    f=s[i:j+1]
    return(f==f[::-1])
def matchain(st,i,j):
    if i>=j:
        return(0)
    if ispalindrome(st,i,j):
        return(0)
    if dp[i][j]!=-1:
        return dp[i][j]
    else:
        maxi=float("inf")
        for k in range(i,j):
            if dp[i][k]!=-1:
                left=dp[i][k]
            else:
                left=matchain(st,i,k)
            if dp[k+1][j]!=-1:
                right=dp[k+1][j]
            else:
                right=matchain(st,k+1,j)
            temp=left+right+1
            if temp<maxi:
                maxi=temp
        dp[i][j]=maxi
        return(dp[i][j])
s="abtin"
n=len(s)
dp=[[-1 for i in range(n)]for j in range(n)]
print(matchain(s,0,(n-1)))
for i in dp:
    print(i)