# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:35:58 2020

@author: DELL
"""

l=input()
e=len(l)
r=len(l)//2
flag=0
for i in range(r,0,-1):
    if l[0:i]==l[(e-i):]:
        print(i)
        flag=1
        break
if flag==0:
    print(0)
