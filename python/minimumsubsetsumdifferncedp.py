#bottom up
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
    return(dp)
arr=[2,3,7]
n=len(arr)
sumi=sum(arr)
dptable=subsetsum(arr,sumi)
l=[]
for i in range((sumi//2)+1):
    if dptable[n][i]==True:
        l.append(i)
mini=sumi
for i in range(len(l)):
    if sumi-(2*l[i])<mini:
        mini=sumi-(2*l[i])
print(mini)
