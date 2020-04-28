# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:41:56 2020

@author: DELL
"""

t=input()
l=[]
for i in range(1,len(t),2):
    l.append(int(t[i]))
for i in range(len(l)):
    l[i]=l[i]*l[i]
for i in range(len(l)):
    l[i]=str(l[i])
print(l)
fu="".join(l)
print(fu[:4])