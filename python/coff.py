n,k=map(int,input().split(' '))
l=list(map(int,input().split()))
l.sort()
l=l[:k]
print(l)
oddl=[]
evenl=[]
for i in range(k):
    if (i+1)%2==0:
        evenl.append(l[i])
    else:
        oddl.append(l[i])
oddl.sort()
evenl.sort()
print(evenl)
print(oddl)
print(
'''mini=float("inf")
kj=len(oddl)
nj=len(evenl)
if nj<=kj:
    for i in range(1,min(nj+1,k)):
        if (k-i)<=kj:
            minc=min(evenl[i-1],oddl[k-i-1])
            mini=min(mini,minc)
    if kj>=k:
        mini=min(mini,oddl[k-1])
else:
    for i in range(1,min(kj+1,k)):
        if (k-i)<=nj:
            minc=min(oddl[i-1],evenl[k-i])
            mini=min(minc,mini)
    if nj>=k:
        mini=min(mini,evenl[k-1])
print(mini)'''