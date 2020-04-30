class Solution:
    def findTargetSumWays(self, nums:List[int], S: int) -> int:
        def countsubset(arr,sum):
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
        sumi=sum(nums)
        if (S+sumi)%2!=0 or S>sumi:
            return(0)
        else:
            return(countsubset(nums,((S+sumi)//2)))