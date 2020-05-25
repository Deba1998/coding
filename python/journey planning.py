n=int(input())
arr=list(map(int,input().split()))
x=dict()
for i in range(n):
    if (i+1-arr[i]) in x:
        x[(i+1-arr[i])]+=arr[i]
    else:
        x[(i+1-arr[i])]=arr[i]
maxi=0
for i in x:
    if x[i]>maxi:
        maxi=x[i]
print(maxi)
