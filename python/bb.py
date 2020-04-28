'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def dfs(l,colour):
    for i in range(l):
        if colour==x[l[i]]:
            if l[i] not in kj:
                
   
t=int(input())
l=[[]for i in range(100000)]
for i in range(t-1):
    x, y=map(int,input().split())
    l[x-1].append(y-1)
k=list(map(int,input().split()))
x=dict()
for i in range(len(k)):
    if i not in x:
        x[i]=k[i]
q=int(input())
count=0
kj=dict()
for k in range(q):
    y=int(input())
    if t==1:
        if y==1:
            count=1
        else:
            count=0
    else:     
        if (y-1) not in kj:
            kj[y-1]=1
            count+=1
        if len(l[y-1])>0:
            for i in range(len(l[y-1])):
                if x[y-1]==x[l[y-1][i]]:
                    if l[y-1][i] not in kj:
                        kj[l[y-1][i]]=1
                        count+=1
    print(count)
