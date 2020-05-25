from sys import setrecursionlimit
setrecursionlimit(10**9+7)
def solve(s,n):
    p=(10**9)+7
    if n==0 or n==1:
        return(1)
    if dp[n]!=-1:
        return(dp[n])
    elif s[n-1]==s[n-2] and (s[n-1]=="u" or s[n-1]=="n"):
        dp[n]=(solve(s,n-1)%p+solve(s,n-2)%p)%p
        return(dp[n])
    else:
        dp[n]=solve(s,n-1)%p
        return(dp[n])
s=input()
n=len(s)
flag=0
for i in range(n):
    if s[i]=="m" or s[i]=="w":
        flag=1
        break
if flag==1:
    print(0)
else:
    dp=[-1 for i in range(n+1)]
    print(solve(s,n))
    