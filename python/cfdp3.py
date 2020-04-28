import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
l=list(map(int,input().split()))
ans=0
if l[0]>=0:
    ans+=1
if l[-1]<=0:
    ans+=1
neg=[0]*(len(l)-1)
pos=[0]*(len(l)-1)
for i in range(1,len(l)-1):
    if l[i]<0:
        neg[i]=neg[i-1]
    else:
        neg[i]=neg[i-1]+1
for i in range(len(l)-3,-1,-1):
    if l[i+1]>0:
        pos[i]=pos[i+1]
    else:
        pos[i]=pos[i+1]+1
mini=1000001
for i in range(n-1):
    mini=min(mini,(pos[i]+neg[i]))
print(ans+mini)