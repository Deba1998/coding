# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:50:12 2020

@author: DELL
"""

import itertools
l=list(map(int,input().split(',')))
s=int(input())
k=list(itertools.combinations(l,4))
print(k)
count=0
for i in k:
    if sum(i)==s:
        count+=1
print(count)