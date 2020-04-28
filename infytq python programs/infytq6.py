# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:23:02 2020

@author: DELL
"""

s=input()
l=[]
for i in s:
    if i.isdigit():
        l.append(i)
s=set(l)
r=list(s)
r.sort()
flag=0
for i in r:
    if int(i)%2==0:
        flag=1
        y=i
        r.remove(y)
        break
if flag==0:
    print(-1)
else:
    r.sort(reverse=True)
    q="".join(r)
    q+=y
    print(q)

    