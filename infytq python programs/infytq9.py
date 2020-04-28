# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:34:05 2020

@author: DELL
"""

l=list(map(int,input().split(",")))
r=l.index(5)
t=l[0:]
for i in range(len(t)):
    t[i]=str(t[i])
s="".join(t)
ri=s.rindex("8")
w=l[:r]+l[ri+1:]
e=l[r:ri+1]
for i in range(len(e)):
    e[i]=str(e[i])
sumu=sum(w)
g="".join(e)
g=int(g)
sumu=sumu+g
print(sumu)
