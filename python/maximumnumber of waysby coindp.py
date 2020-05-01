#assume coint is always positive and greater than 0
#bottom up
def countsubset(arr,sum):
    n=len(arr)
    dp=[[0 for i in range(sum+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if j==0:
                dp[i][j]=1
            elif i==0 and j!=0:
                dp[i][j]=0
            elif arr[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return(dp[n][sum])
arr=[1,2,3]
sum=5
print(countsubset(arr,sum))
'''#top down
def countsubset(arr,sum,n):
    if sum==0:
        return 1
    if n==0 and sum!=0:
        return 0
    if dp[n][sum]!=-1:
        return(dp[n][sum])
    elif arr[n-1]<=sum:
        dp[n][sum]=countsubset(arr,sum,n-1)+countsubset(arr,sum-arr[n-1],n)
    else:
        dp[n][sum]=countsubset(arr,sum,n-1)
    return(dp[n][sum])
arr=[1,2,3]
n=len(arr)
sum=5
dp=[[-1 for i in range(sum+1)]for i in range(n+1)]
print(countsubset(arr,sum,n))'''
