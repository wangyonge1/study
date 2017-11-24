#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
数字类型练习
'''
def mul(num1,num2):
    if isinstance(num1,(int,long,float)) and \
       isinstance(num2,(int,long,float)):
       return num1*num2
    else:
        print "num1 or num2 type error" 
def score(num):
    if isinstance(num,int):
        if 90<=num<=100:
            return 'A'
        elif 80<=num<=89:
            return 'B'
        elif 70<=num<=79:
            return 'C'
        elif 60<=num<=69:
            return 'D'
        elif 0<num<=59:
            return 'F'
        else:
            print "num range error"
    else:
        print "num type error"  
def isLeap(year):
    if isinstance(year,int) and 1000<year<10000:
        if (year%4==0 and year%100!=0)or(year%400==0):
            return True
        else:
            return False

    else:
        print 'year input error'        
def money(m):
    m25=0
    m10=0
    m5=0
    m1=0
    sheng=0
    if m//25>0:
        m25=m//25
        sheng=m-m25*25
    if sheng//10>0:
        m10=sheng//10
        sheng-=m10*10
    if sheng//5>0:
        m5=sheng//5
        sheng-=m5*5
    if sheng//1>0:
        m1=sheng

    return m25,m10,m5,m1
def cal(s):
    l=s.split()
    
    num1=float(l[0])
    num2=float(l[2])
    
    
    operator=l[1]
    if isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        if operator=='+':
            return num1+num2
        elif operator=='-':
            return num1-num2
        elif operator=='*':
            return num1*num2
        elif operator=='/':
            return num1/num2
        else:
            print "operator error"
    else:
        print "num is error"  
print [x for x in range(21) if x%2==0]






        
        
        

