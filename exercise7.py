#!/usr/bin/env python
# _*_ coding:utf-8 _*_

 
import string    
def rot13(s):
    "exercise 7-10"
    mi={}
    l=[]
    alph=string.letters[:26]
    for i in range(26):
        if i<13:
            mi[alph[i]]=alph[i+13]
        else:
            mi[alph[i]]=alph[i-13]
    for j in s:
        if j in string.letters:
            if j.islower():
                l.append(mi[j])
            else:
                l.append(mi[j.lower()].upper())
        else:
            l.append(j)
    return ''.join(l)
def tr(srcstr,dststr,str):
    "exercise 7-9"
    dic={}
    l=[]
    
    if len(srcstr)<len(dststr):
        for i in range(len(srcstr)):
            dic[srcstr[i].lower()]=dststr[i]
    else:
        for i in range(len(dststr)):
            dic[srcstr[i].lower()]=dststr[i]
        for j in range(len(dststr),len(srcstr)):
            dic[srcstr[j].lower()]=None
    
    for c in str:
        if c in dic :
            if dic[c]!=None:
                l.append(dic[c])
            else:
                pass
        else:
            l.append(c)
    return ''.join(l)
    
def stock():
    'exercise 7-6'
    i=0
    l=[]
    dic={}
    while i<5:
        tmp=[]
        sn1=raw_input('sn:').strip()
        sn2=raw_input('sn:').strip()
        sn3=raw_input('sn:').strip()
        sn4=raw_input('sn:').strip()
        tmp.append(sn1)
        tmp.append(sn2)
        tmp.append(sn3)
        tmp.append(sn4)
        l.append(tmp)
        i+=1
    for i in range(len(l)):
        dic[l[i][0]]=[l[i][1],l[i][2],l[i][3]]
    for i in sorted(dic):
        print i,dic[i]


  
         


