# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:28:13 2020

@author: DELL
"""

s=input()
t=[]
for i in range(len(s)):
    if s[i]!='@' and s[i]!='#':
        t.append(s[i])
t.reverse()
for i in range(len(s)):
    if s[i]=="@" or s[i]=="#":
       t.insert(i,s[i])
print("".join(t))