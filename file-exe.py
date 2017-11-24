#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
读取文件，并编辑其中一行，并保存
'''
import os
sep=os.linesep



def writef(fname,ln,lc,issave,fc):#fc不能通过全局变量传递
    
    if issave=='y':
        try:
            fp=open(fname,'w+')
            
            
            for i in range(len(fc)):
                if i==int(ln)-1:
                    fc[i]=lc
                fp.writelines("%s%s" %(fc[i].rstrip(),sep))
            
            if len(fc)<int(ln):
                fp.writelines('%s%s'%(lc,sep))
            #fp.flush()
                    
        except IOError,e:
            print "io error %s" %e
        finally:
            if fp:
                fp.close()
    else:
        print "no save"                

def gettext():
    line=raw_input('input hang hao:')
    while True:
        try:
            isinstance(int(line),int)
            if 0<int(line):
                new=raw_input('input new content:')
                issave=raw_input('input "y" save,other not save:')
                break
            else:
                line=raw_input('input hang(1-5) hao:')

            
        except:
            print "input type error"
            line=raw_input('input hang hao:')
    return line,new ,issave           
def readf(fname):
    try:
        fp=open(fname,'r+')
        fc=fp.readlines()
        #test=fc
        return fc
    except:
        print "io error"
    finally:
        if fp:
            fp.close()
fc=readf('text.txt')
line,new,issave=gettext()

writef('text.txt',line,new,issave,fc)            


        
        
        

