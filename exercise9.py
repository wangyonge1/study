#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os,pickle
def commentfile():
    'exercise 9-1'
    try:
        f=open('read1.txt','r')
        f1=open('write.txt','w')
        for i in f:
            i=i.strip()
            index=i.find('#')
            if index==-1 :
                f1.write('%s%s' %(i,os.linesep))
            elif index==0:
                pass
            else:
                f1.write('%s%s' % (i[0:index],os.linesep))

    except IOError:
        print 'read file error'
    finally:
        print 'finally....'
        f.close()
        f1.close()
def fileaccess(fname,num):
    'exercise 9-2'
    try:
        f=open(fname,'r')
        count =0
        for i in f:
            if count == num:
                break
            print i.strip()
            count+=1
    except IOError:
        print "open file error"
    finally:
        f.close()
def fileaccess(fname):
    'exercise 9-3'
    try:
        f=open(fname,'r')
        count =0
        for i in f:
            
            count+=1
        return count
    except IOError:
        print "open file error"
    finally:
        f.close()
def fileaccesspage(fname,num):
    'exercise 9-4'
    try:
        f=open(fname,'r')
        count =0
        for i in f:
            if count == num:
                count =0
                ispage=raw_input('请按任意键继续。。。')
            print i.strip()
            count+=1
    except IOError:
        print "open file error"
    finally:
        f.close()
def cmpfile(fname1,fname2):
    'exercise 9-6 已实现：不同行数和不同列数'
    f1=open(fname1)
    f2=open(fname2)
    l1=[x for x in f1]
    l2=[y for y in f2]
    l=map(None,l1,l2)
    line =1
    issame=True
    for x,y in l:
        if x != None and y!=None:
            if cmp(x.strip(),y.strip()):
                issame=False
                for i in range(min(len(x),len(y))):
                    if x[i]!=y[i]:#如果长度不相等，换行符参与比较
                        break

                print line,i+1
        else:
            issame = False
            print line,1 
            break       
        line +=1
    if issame==True:
        print 'file equal'
    f1.close()
    f2.close()
#练习9-7 解析win.ini文件
def parsefile(fname):
    filedic={}
    try:
        f=open(fname,'r')
        for line in f:
            indexbrace=line.find(']')
            indexequal=line.find('=')
            if line[0]=='[' and indexbrace!=-1:
                newkw=line.strip()
                tmpdic={}
                filedic[newkw[1:indexbrace]]=tmpdic
            elif indexequal!=-1:
                tmpdic[line[:indexequal]]=line[indexequal+1:]
        # for i,j in filedic.items():
        #     print '['+i+']'
        #     for x,y in j.items():
        #         print x+'='+y,
        return filedic
    except IOError:
        print 'open file error'
    finally:
        f.close()
def serialize(fname1):
    dic=parsefile('win.ini')
    f1=open(fname1,'wb')
    pickle.dump(dic,f1)
    f1.close()
    
    f2=open(fname1,'rb')
    dic=pickle.load(f2)
    f2.close()
    print dic
    


#练习9-16 截断文件中大于80个字符的行
def linebreak(fname1,fname2):
    sep=[' ',';','.','?','!',',']
    try:
        f1=open(fname1,'r')
        f2=open(fname2,'w')
        for line in f1:
            newline=line.strip()
            while newline:
                if len(newline)<=80:
                    f2.write('%s%s' %(newline.strip(),os.linesep))
                    newline=''
                else:
                    for i in range(80,0,-1):
                        
                        if newline[i] in sep:
                            break

                    f2.write('%s%s' %(newline[:i].strip(),os.linesep))
                    newline=newline[i+1:]

    except IOError:
        print 'open file error'
    
    finally:
        f1.close()
        f2.close()
















           
  
         


