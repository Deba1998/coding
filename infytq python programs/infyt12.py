# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:13:50 2020

@author: DELL
"""

l=input()
y=dict()
for i in range(len(l)):
    if l[i].lower() not in y:
        uys=l[i].lower()
        y[uys]=[l[i]]
    else:
        if l[i].lower() in y:
            uys=l[i].lower()
            y[uys].append(l[i])
r=[]
for values in sorted(y.keys()):
    r.append(y[values])
for i in range(len(r)):
    r[i]="".join(r[i])
t=len(r)//2
if len(r)%2==0:
    s=""
    for i in range(t):
        s=s+r[i]+r[(len(r)-1)-i]
else:
    s=""
    for i in range(t):
        s=s+r[i]+r[(len(r)-1)-i]
    s=s+r[t]
print(s)
    