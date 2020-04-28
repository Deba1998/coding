#chain
def maxpairs(l):
    l.sort()
    n = len(l)
    arr = [1]*n
    for i in range(1,n):
        for j in range(i):
            if(l[j][1]<l[i][0]):
                arr[i] =max(arr[j]+1,arr[i])
    return arr[n-1]
li= [(5,24),(25,26),(27,40),(39,60),(15,28),(50,90)]
print(maxpairs(li))