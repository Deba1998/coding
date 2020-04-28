# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:32:44 2020

@author: DELL
"""

w=input()
r=input()
x=dict()
y=dict()
for i in w:
    if i not in x:
        x[i]=1
    else:
        x[i]+=1
for j in r:
    if j not in y:
        y[j]=1
    else:
        y[j]+=1
count=0
for i in x:
    if i in y:
        count+=min(x[i],y[i])
print((len(w)-count)+(len(r)-count))