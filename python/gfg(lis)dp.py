#lis
def lis(l):
    lis=[1]*len(l)
    for i in range(1,len(l)):
        for j in range(i):
            if l[i]>l[j]:
                lis[i]=max(lis[i],(lis[j]+1))
    return(max(lis))
arr=[1,3,8,2,9]
print(lis(arr))