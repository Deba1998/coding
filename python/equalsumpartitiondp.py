'''#bottom up
def subsetsum(arr,sum):
    n=len(arr)
    dp=[[0 for i in range(sum+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if j==0:
                dp[i][j]=True
            elif i==0 and j!=0:
                dp[i][j]=False
            elif arr[i-1]<=j:
                dp[i][j]=(dp[i-1][j] or dp[i-1][j-arr[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    return(dp[n][sum])
arr=[2,3,7,8,10]
n=len(arr)
sum=sum(arr)
if sum%2!=0:
    print(False)
else:
    print(subsetsum(arr,sum//2))'''
#topdown
def subsetsum(arr,sum,n):
    if sum==0:
        return(True)
    if n==0 and sum!=0:
        return(False)
    if dp[n][sum]!=-1:
        return(dp[n][sum])
    if arr[n-1]<=sum:
        dp[n][sum]=subsetsum(arr,sum,n-1) or subsetsum(arr,sum-arr[n-1],n-1)
    else:
        dp[n][sum]=subsetsum(arr,sum,n-1)
    return(dp[n][sum])
arr=[2,2,8,8,10]
n=len(arr)
sum=sum(arr)
if sum%2!=0:
    print(False)
else:
    dp=[[-1 for i in range(sum+1)]for i in range(n+1)]
    print(subsetsum(arr,sum//2,n))