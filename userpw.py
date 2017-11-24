#!/usr/bin/env python
#_*_coding:utf-8_*_
import time
db={}
def newuser():
    username=raw_input('please input username:').lower()
    if username in db:
        print 'username is exist,try another...'
    else:
        pwd=raw_input('please input your password:')
        db[username]=[pwd,0]
def olduser():
    loginuser=raw_input('please input your login name:').lower()
    pwd=raw_input('please input your password:')
    passwd=db.get(loginuser)[0]#登录操作
    if passwd==pwd:
        logintime=time.time()
        if (logintime-db[loginuser][1])>4*60*60:
            db[loginuser]=[pwd,logintime]
            print 'welcome!'
        else:
            strtime=time.localtime(time.time())
            print 'you  logged at ',time.strftime('%Y-%m-%d %H:%M:%S',strtime)
    else:
        print 'user not correct'
def user():
    count=0#密码最多输错3次
    while count<3:
        loginuser=raw_input('please input your login name:').strip().lower()
        pwd=raw_input('please input your password:').strip()
        tmpuser=loginuser.replace('_','a')
        if len(loginuser)<=0 or len(pwd)<=0 or  not tmpuser.isalnum():
            continue

        if loginuser in db:
            if db[loginuser][0]==pwd:
                count=0
                logintime=time.time()
                if (logintime-db[loginuser][1])>4*60*60:
                    db[loginuser]=[pwd,logintime]
                    print 'welcome!'
                    break
                else:
                    strtime=time.localtime(db[loginuser][1])
                    print 'you  logged at ',time.strftime('%Y-%m-%d %H:%M:%S',strtime)
                    break
            else:
                count += 1
                print 'user not correct'
                continue
        else:
            choice = raw_input('add a user y/n...').strip().lower()
            if choice =='y':
                db[loginuser]=[pwd,0]
                break
            else:
                print 'user not correct'
                break
    
def deluser():
    username=raw_input('please input delete username:').strip().lower()
    if username in db:
        db.pop(username)
        print 'delete complete'
    else:
        print 'user not exist'
def listuser():
    for i,j in db.items():
        print 'user:%s,pwd:%s' % (i,j[0])
        
def showmenu():
    CMDS={'n':newuser,'o':olduser,'u':user,'d':deluser,'l':listuser}
    pr='''
    options:
    (N)ewuser
    (O)lduser
    (U)ser
    (D)eleteuser
    (L)istuser
    (Q)uit
    '''   
    while True:#对用户操作的外层循环
        while True:#menu选择的内层循环
            try:
                choice=raw_input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt):
                choice='q'
            if choice in 'noquld':
                break
        if choice=='q':
            break
        else:
            CMDS[choice]()
if __name__=='__main__':
    showmenu()



