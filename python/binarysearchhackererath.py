import math
def possible(arr,brr,h,n,m):
    if h%2==0:
        cou=h//2
    else:
        cou=(h//2)+1  
    if cou>=n:
        return(True)
    else:
        n=n-1-cou
        j=m-2
        flag=0
        while j>=0 and n>=0:
            if arr[n]<=brr[j]:
                j-=1
                n=n-cou
            else:
                flag=1
                break
        if n+1>0:
            flag=1
        if flag==1:
            return(False)
        else:
            return(True)    
n,m=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))
arr.sort()
brr.sort()
low=1
high=n*2
ans=n**2
while low<=high:
    mid=low+(high-low)//2
    if possible(arr,brr,mid,n,m):
        ans=min(ans,mid)
        high=mid-1
    else:
        low=mid+1
print(ans)
    



