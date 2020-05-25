s=input()
n=len(s)
l=[]
k=[]
for i in range(n-1):
    if s[i]=="A" and s[i+1]=="B":
        l.append([i+1,i])
    if s[i]=="B" and s[i+1]=="A":
        k.append([i,i+1])
if len(l)==0 or len(k)==0:
    print("NO")
else:
    if abs(len(l)-len(k))>0 and (len(l)>2 or len(k)>2):
        flag=1
    else:
        flag=0
        for i in range(len(l)):
            if l[i][0]!=k[0][0] and l[i][1]!=k[0][1]:
                flag=1
                break
        for i in range(len(k)):
            if k[i][0]!=l[0][0] and k[i][1]!=l[0][1]:
                flag=1
                break
    if flag==1:
        print("YES")
    else:
        print("NO")

