#!/usr/bin/env python
# _*_ coding:utf-8 _*_

queue=[]
def enQ():
    queue.append(raw_input('enter new string:').strip())
def deQ():
    if len(queue)==0:
        print 'cannot pop from an empty queue'
    else:
        print 'removed[',`queue.pop(0)`,']'#如果从末尾移出：pop()
def viewQ():
    print queue
CMDs={'e':enQ,'d':deQ,'v':viewQ}
def showmenu():
    pr='''
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit
    enter choice
    '''
    while True:
        while True:
            try:
                choice=raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice='q'
            if choice not in 'devq':
                print "try again"
            else:
                break
        if choice=='q':
            break
        CMDs[choice]()
if __name__=='__main__':
    showmenu()        
