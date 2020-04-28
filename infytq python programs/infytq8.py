# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:37:41 2020

@author: DELL
"""

i=input()
q=i.split(",")
gist=[]
for i in q:
    l=[]
    temp=i.split(":")
    name=temp[0]
    number=temp[1]
    for g in number:
        l.append(int(g))
    for i in range(len(l)):
        l[i]=l[i]**2
    if sum(l)%2==0:
        rty=name[len(name)-2:]+name[:len(name)-2]
        gist.append(rty)
    else:
        rty=name[1:]+name[0]
        gist.append(rty)
print(" ".join(gist))
        