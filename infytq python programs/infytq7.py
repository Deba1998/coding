# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:12:53 2020

@author: DELL
"""

l=input()
maxi=""
for i in range(0,len(l)):
    for j in range(i,len(l)):
        s=l[i:(j+1)]
        if len(s)>3 and len(set(s))==len(s):
            if len(maxi)<len(s):
                maxi=s
        if len(set(s))<len(s):
            break
if len(maxi)==0:
    print(-1)
else:
    print(maxi)
        
                
            