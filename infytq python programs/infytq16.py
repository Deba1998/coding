# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:19:10 2020

@author: DELL
"""

string=input()
even=[]
odd=[]
special_char=0
for ch in string:
    if(ch.isalnum() == False):
        special_char+=1
    elif(ch.isdigit()):
        if int(ch)%2==0:
            even.append(ch)
        else:
            odd.append(ch)
            
if(special_char%2!=0):
      odd,even=even,odd             
even_len=len(even)
odd_len=len(odd)
m=max(even_len,odd_len)
e=0
o=0
r=[]
for i in range(m):
    if(e!=even_len):
        r.append(even[e])
        #print(even[e],end='')
        e+=1
    if(o!=odd_len):
        r.append(odd[o])
        #print(odd[o],end='')
        o+=1
print("".join(r))