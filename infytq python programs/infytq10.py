# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:47:26 2020

@author: DELL
"""

t=int(input())
num=list(map(int,input().split(' ')))
ti=sorted(num,key=num.count)
while t>0:
    ti.remove(ti[0])
    t-=1
y=list(set(ti))
print(len(y))