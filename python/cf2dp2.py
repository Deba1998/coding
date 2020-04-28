n=int(input())
a=input()
a=list(a)
b=input()
b=list(b)
cost=0
for i in range(n-1):
    if a[i]!=b[i]:
        if a[i+1]==b[i] and a[i]==b[i+1]:
            a[i+1]=b[i+1]
            cost+=1
        else:
            cost+=1
if a[n-1]!=b[n-1]:
    cost+=1
print(cost)

