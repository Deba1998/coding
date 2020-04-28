m=int(input())
l=list(map(int,input().split()))
n=int(input())
li=list(map(int,input().split()))
l.sort()
li.sort()
i=0
j=0
count=0
while i<m and j<n:
    if abs(l[i]-li[j])<=1:
        count+=1
        i+=1
        j+=1
    else:
        if l[i]>li[j]:
            j+=1
        else:
            i+=1
print(count)


  