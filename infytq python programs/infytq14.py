# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:44:58 2020

@author: DELL
"""

def sumu(l):
    ri=str(l)
    k=[]
    for i in ri:
        k.append(int(i))
    return(l%sum(k)==0)
q=int(input())
l=[]
for i in range(q):
    o=list(map(int,input().split()))
    cou=len(o)
    l.append(o)
result=[]
for i in range(q-1):
    for j in range(cou-1):
        if sumu(l[i][j])==sumu(l[i+1][j])==sumu(l[i][j+1])==sumu(l[i+1][j+1])==True:
            print(l[i][j],l[i][j+1])
            print(l[i+1][j],l[i+1][j+1])
            
            
            '''result.append([l[i][j],l[i][j+1],l[i+1][j],l[i+1][j+1]])
if len(result)==0:
    print("-1")
else:
    for i in range(len(result)):
        print(result[i][0],end=" ")
        print(result[i][1])
        print(result[i][2],end=" ")
        print(result[i][3])'''
            
            
    