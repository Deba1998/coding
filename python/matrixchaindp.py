def matchain(arr,i,j):
    if i>=j:
        return(0)
    if dp[i][j]!=-1:
        return dp[i][j]
    else:
        maxi=float("inf")
        for k in range(i,j):
            temp=matchain(arr,i,k)+matchain(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
            if temp<maxi:
                maxi=temp
        dp[i][j]=maxi
        return(dp[i][j])
arr=[40,20,30,10,30]
n=len(arr)
dp=[[-1 for i in range(n)]for j in range(n)]
print(matchain(arr,1,(n-1)))
for i in dp:
    print(i)