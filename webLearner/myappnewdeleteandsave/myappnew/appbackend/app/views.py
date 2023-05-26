from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *
from venv import create
import datetime
import json
accounts=[]
# Create your views here.
def login(request):
    if request.method=='POST':
        logininfo=json.loads(request.body.decode('utf-8'))
        templogin=logininfo['data']
        user=templogin['user']
        password=templogin['pass']
        check=UserDB.objects.filter(username=user,password=password)
        print(check)
        print(user,password)
        if len(check)==0:
            return HttpResponse(json.dumps('Wrong username or password'))
            
        else:
            return HttpResponse(json.dumps('Success login'))
    return HttpResponse('hi')

def signUp(request):
    if request.method=='POST':
        signinfo=json.loads(request.body.decode('utf-8'))
        signinfotemp=signinfo['data']
        user=signinfotemp['newuser']
        password=signinfotemp['newpass']
    #before we insert account to User,Db we need to check 
    #whether there is a username that is the same as that one or not
        
        
        checkuser=UserDB.objects.filter(username=user)

        print(checkuser)
        if len(checkuser)==0:
            UserDB.objects.create(username=user,password=password)
            return HttpResponse(json.dumps('success'))
        else:
            return HttpResponse(json.dumps('Fail'))
        
        

        
    return HttpResponse('SignUp backend')
def changepassMain(request):
    from .models    import UserDB
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        print(data)
        tempdata=data['data']
        print(tempdata)
        user=tempdata['user']
        password=tempdata['pass']
        checkuser=UserDB.objects.filter(username=user,password=password)
       
        
        if len(checkuser)==1:
            newpassword=tempdata['newpass']
            checkuser=UserDB.objects.filter(username=user,password=password).update(password=newpassword)
            #account=UserDB.objects.get(username=user,password=password)
            #account.password=newpassword
            #account.save()
            return HttpResponse(json.dumps({"msg":"update successfully"}))
        else:
            return HttpResponse(json.dumps({"msg":"account does not exist"}))

        
        
    return HttpResponse('Hello World')

def userprofile(request):
    from .models    import UserInfo
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        tempdata=data['data']
        
        user=tempdata['user']#This is automatic, user dont type here
        #print(user)
        name=tempdata['name']
        nick=tempdata['nick']
        occupation=tempdata['occupation']
        address=tempdata['address']
        hobby=tempdata['hobby']
        check=UserInfo.objects.filter(username=user)
        #print(check)
        if len(check)==0:
            #print(tempdata)
            UserInfo.objects.create(username=user,name=name,nickname=nick,occupation=occupation,address=address,hobby=hobby)
        else:
            check=UserInfo.objects.filter(username=user).update(username=user,name=name,nickname=nick,occupation=occupation,address=address,hobby=hobby)
        #print(data)
        #print(tempdata)
        return HttpResponse(json.dumps('it works'))
    return HttpResponse('Profile backend')

def getprofile(request):
    from .models import UserInfo
    #homework:
    #get username from fetch
    #our bbackend will get userInfo base on username
    #code look like user.info.objects.filter(username=user)
    #we can make a json dump return look like {'name':'marco','occcupation':programmer,....}
    #return this json to frontend to then seperate it and make it inner.text
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        user1=data['username']
        #print(user1)
        info1=UserInfo.objects.get(username=user1)
        
        
        #info1=info[0]
        #print(info1)
        
        
        name=info1.name
        #print(name)
        nick=info1.nickname
        occu=info1.occupation
        addr=info1.address
        hob=info1.hobby
        back={'name':name,'nick':nick,'occ':occu,'add':addr,'hobb':hob}
        
        return HttpResponse(json.dumps(back))
    return HttpResponse('Helloworld2')


#logic path is backend functions
#render path is how the website look, website design
#create blog area

def blogdata(request):
    from .models import BlogInfo
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        print('this works')
        print(data)
        title=data['title']
        content=data['content']
        time=datetime.datetime.now()
        rettime=time.year,time.month,time.day
        #print(rettime)
        BlogInfo.objects.create(title=title,blogdata=content,timerecord=time)
        strtime=str(time.year)+'/'+str(time.month)+'/'+str(time.day)
        returnData={'title':title,'content':content,'time':strtime}
        print(returnData)
        return HttpResponse(json.dumps('hello'))

    return HttpResponse('Hello world 3')

def getBlog(request):
    if request.method=='POST':
        #data=json.loads(request.body.decode('utf-8'))
        #print(data,'It received the data')
        lst=BlogInfo.objects.all()
        res=[]
        print(lst)
        for i in lst:
            temp=[]
            temp.append(i.id)
            temp.append(i.title)
            res.append(temp)
        print(res)
        return HttpResponse(json.dumps(res))

    return HttpResponse('hello world 4')

def bloginfo(request):
    from .models import BlogInfo
    if request.method=='POST':
        id=json.loads(request.body.decode('utf-8'))
        getId=BlogInfo.objects.get(id=id)
        title=getId.title
        blogdata=getId.blogdata
        time=getId.timerecord
        data={'title':title,'blogdata':blogdata,'time':str(time)}
        return HttpResponse(json.dumps(data))
    return HttpResponse('blog backend for information')

def updateBlog(request):
    from .models import BlogInfo
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        
        print(data)
        newtitle=data['title']
        datasent=data['datasent']
        id=data['id']
        print(datasent,id)
        BlogInfo.objects.filter(id=id).update(blogdata=datasent)
        if len(newtitle)==0:
            pass
        else:
            BlogInfo.objects.filter(id=id).update(title=newtitle)
        return HttpResponse(json.dumps('hi'))
    return HttpResponse('update blog backend')

def deleteBlog(request):
    from .models import BlogInfo
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))
        print(data)
        id=data
        BlogInfo.objects.filter(id=data).delete()
        return HttpResponse(json.dumps('connect'))
    return HttpResponse('delete blog backend')