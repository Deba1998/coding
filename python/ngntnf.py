s="101"
d=2
l=list(s)
l=[0]+l
n=len(s)
count=0
ficount=0
for i in range(1,n+1):
    if l[i]=="1":
        count+=1
    if i%(d)==0:
        if count==0:
            ficount+=1
        else:
            count=0
print(ficount)
h=l[n+1-d:n+1]
print(h)
if h.count(1)==0:
    ficount+=1
print(ficount)