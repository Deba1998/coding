#lis
def lis(l):
    lis=[1]*(len(l)+1)
    for i in range(1,(len(l)+1)):
        for j in range(i*2,len(l)+1,i):
            if l[i-1]<l[j-1]:
                lis[j]=max(lis[j],(lis[i]+1))
    return(max(lis))
n=int(input())
for i in range(n):
    k=int(input())
    l=list(map(int,input().split()))
    print(lis(l))
