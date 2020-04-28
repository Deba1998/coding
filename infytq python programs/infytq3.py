# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:50:49 2020

@author: DELL
"""

s=input()
count=0
sta=[]
for i in range(len(s)):
    if s[i]=="(" or s[i]=="{" or s[i]=="[":
        sta.append(s[i])
    else:
        if len(sta)==0:
            print(i+1)
            count+=1
            break
        else:
            ry=sta.pop()
            if s[i]=="]" and ry!="[":
                print(i+1)
                count+=1
                break
            elif s[i]=="}" and ry!="{":
                print(i+1)
                count+=1
                break
            elif s[i]==")" and ry!="(":
                print(i+1)
                count+=1
                break
if count==0 and len(sta)==0:
    print(0)
elif count==0 and len(sta)!=0:
    print(len(s)+1)
    
    