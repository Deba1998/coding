# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:22:04 2020

@author: DELL
"""

o=list(input().split(","))
r=[]
for i in o:
    temp=i.split(":")
    name=temp[0]
    number=temp[1]
    ry=len(name)
    maxi=0
    for j in number:
        if int(j)<=ry:
            if int(j)>maxi:
                maxi=int(j)
    if maxi==0:
        r.append("X")
    else:
        r.append(name[maxi-1])
ui="".join(r)
print(ui)    
    
