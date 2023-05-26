from django.shortcuts import render
from django.http.response import HttpResponse
from .models import UserDB
from venv import create
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