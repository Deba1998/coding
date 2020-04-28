# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:19:15 2020

@author: DELL
"""

x=input()
l=[]
for i in x:
    l.append(int(i))
n=len(l)
k=n//2
for i in range(0,k):
    while l[i]!=l[n-1-i]:
        if l[i]<l[n-1-i]:
            l[n-i-1]=l[i]
            l[n-2-i]=l[n-2-i]+1
        else:
            l[n-1-i]=l[i]
s=""
for i in range(0,n):
    s+=str(l[i])
s.join(s)
print(s)