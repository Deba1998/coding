n=int(input())
d=[0]*((10**5)+1)
l=list(map(int,input().split()))
for i in range(n):
    d[l[i]]+=l[i]
dp=[0]*((10**5)+1)
dp[1]=d[1]
for i in range(2,(10**5)+1):
    dp[i]=max(dp[i-1],dp[i-2]+d[i])
print(dp[-1])