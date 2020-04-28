# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:13:50 2020

@author: DELL
"""

l=list(map(int,input().split(",")))
length=len(l)
listtotal=[]
for i in range(0,length-1):
    for x in range(i+1,length):
        first=l[i]
        second=l[x]
        fablist=[]
        fablist.append(first)
        fablist.append(second)
        for y in range(x+1,length):
            if(first+second==l[y]):
                fablist.append(l[y])
                first=second
                second=l[y]
        if len(listtotal)<len(fablist):
            listtotal=fablist
if len(listtotal)>2:
    print(listtotal)
else:
    print(-1)
