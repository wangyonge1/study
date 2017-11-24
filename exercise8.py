#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from math import sqrt
 
def isprime(n):
    'exercise 8-4'
    if n<=1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
        
#filter(isprime,range(1,20))
def getfactors(n):
    'exercise 8-5'
    l=[]
    if n<=1:
        return
    for i in range(1,n+1):
        if n % i == 0:
            l.append(i)
    return l
def getprimefactors(n):
    'exercise 8-6'
    primel=[]
    tmp=1
    while tmp < n:
        i = n / tmp
        l=getfactors(i)
        for i in l:
            if isprime(i):
                primel.append(i) 
        tmp=reduce(lambda x,y:x*y,primel)
    return primel
#print sorted(getprimefactors(50))
def isperfect(n):
    'exercise 8-7'
    l=getfactors(n)
    sum=0
    for i in l[:-1]:
        sum += i
    if sum == n:
        return True
    else:
        return False
def fact(n):
    'exercise 8-8'
    result=reduce(lambda x,y:x*y,range(1,n+1))
    return result
def fibo(n):
    'exercise 8-8斐波那契数列'
    l=[1,1]
    while len(l)<n:
        l.append(l[-1]+l[-2])
    return l[-1]
import string
def character(s):
    'exercise 8-10'
    county=0
    countf=0
    l=['a','e','i','o','u']
    for i in s:
        if i.lower() in l:
            print "yuan",i
            county +=1
        elif i in string.letters and i.lower() not in l:
            
            countf +=1
    word=len(s.split())
    return county,countf,word
def text():
    'exercise 8-11'
    count =0
    fail = 0
    l=[]
    while count <5 and fail<3 :
        name=raw_input('please input your name %d:' % count)
        if name.find(',') !=-1 :
            l.append(name)
        else:
            
            fail+=1
            print 'wrong format...%d' %(fail)
        count +=1
    return sorted(l)





           
  
         


