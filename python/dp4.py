s=input()
if len(s)==1:
    print(s)
else:
    l=[]
    for i in s:
        l.append(i)  
    if l[1]==l[0]:
        if l[0]=="z":
            l[1]=="a"
        else:
            l[1]=chr(ord(l[0])+1)
    for i in range(2,len(s)):
        if l[i]==l[i-1]:
            l[i]=l[i-2]
    print("".join(l))