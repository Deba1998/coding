# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:58:11 2020

@author: DELL
"""

def ispalindrome(s):
    z=s[::-1]
    '''l=[]
    for i in s:
        l.append(i)
    l.reverse()
    z="".join(l)'''
    return(z==s)
s=input()
max=0
st=[0]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        yt=s[i:j]
        if ispalindrome(yt):
            w=len(yt)
            if w>max:
                max=w
                st[0]=yt
print(st[0])
                
            
        
        