#bottom up
'''def countsubset(arr,sum):
    n=len(arr)
    dp=[[0 for i in range(sum+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if j==0 and i==0:
                dp[i][j]=1
            elif i==0 and j!=0:
                dp[i][j]=0
            elif arr[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return(dp[n][sum])
arr=[2,3,5,6,8,10]
diff=0
sumi=(sum(arr)+diff)
if sumi%2!=0:
    print(0)
else:
    print(countsubset(arr,(sumi//2)))'''
#top down
def countsubset(arr,sum,n):
    if sum==0 and n==0:
        return 1
    if n==0 and sum!=0:
        return 0
    if dp[n][sum]!=-1:
        return(dp[n][sum])
    elif arr[n-1]<=sum:
        dp[n][sum]=countsubset(arr,sum,n-1)+countsubset(arr,sum-arr[n-1],n-1)
    else:
        dp[n][sum]=countsubset(arr,sum,n-1)
    return(dp[n][sum])
arr=[1,2,3,6,3]
n=len(arr)
diff=13
sumi=(sum(arr)+diff)
if sumi%2!=0:
    print(0)
else:
    dp=[[-1 for i in range((sumi//2)+1)]for i in range(n+1)]
    print(countsubset(arr,sumi//2,n))
