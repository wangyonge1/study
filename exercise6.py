#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
数字类型练习
'''
#一个字符串，每次砍掉最后一个字符显示
# s='abcde'
# for i in [None]+(range(-1,-len(s),-1):
#     print s[:i]

#标识符规则检查
import string,keyword
def identifier(myInput):
    'exercise 6-2'
    al=string.letters+'_'
    num=string.digits
    total=al+num
    myInput=myInput.strip()
    other=myInput[1:]
    try:
        keyword.kwlist.index(myInput)
        print 'kw'
        return False
    except ValueError:
        print 'not keyword'
        if len(myInput)>1:
            if myInput[0] in al:
                for i in other:
                    if i not in total:
                        print "other char error"
                        return False
                return True
            else:
                print "first char error!"
                return False
        elif len(myInput)>0:
            if myInput in string.letters:
                return True
            else:
                return False
        else:
            return False
def debugpy():  
    'exercise 6-7'              
    num_str=raw_input('enter a number:')
    num_num=int(num_str)
    fac_list=range(1,num_num+1)
    print 'before',`fac_list`

    i=0
    lens=len(fac_list)
    while i<lens:
        if num_num % fac_list[i]==0:

            del fac_list[i]
            lens-=1
            i-=1
            #或者将fac_list[i]置为0
            #fac_list[i]=0

        i=i+1
    def fun(*x):
        for i in x:
            if i==0:
                return False
            return True
    #fac_list=filter(None,fac_list)
    fac_list=filter(fun,fac_list)
    print 'after',`fac_list`  
def findchr(s,c):
    'exercise6-12(2)'
    for i,j in  enumerate(s[::-1]):
        if j==c:
            
            break
    else:
        return -1
    return len(s)-i-1

def substr(s,oc,nc):
    "exercise6-12(c)"
    l=[]
    for i in s:
        if i==oc:
            l.append(nc)
        else:
            l.append(i) 

    return ''.join(l) 


  
         


