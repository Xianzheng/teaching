from ast import Pass
from unicodedata import name
from venv import create
from django.shortcuts import render
from django.http.response import HttpResponse
from .model import PasswordPool
from .model import Homework2
from .model import FinalGrade
from django.core import serializers
import json

# Create your views here.
def hello(request):
    obj={'name':'Mark','age':29,'job':'programmer'}
    res=json.dumps(obj)
    return HttpResponse(res)

def postData_view(request):
    if request.method=='GET':
        obj={'name':'Mark','age':29,'job':'programmer'}
        res=json.dumps(obj)
        return HttpResponse(res)
    if request.method=='POST':
        pdata=json.loads(request.body.decode('utf-8'))
        print(pdata)
        print(type(pdata))
        print(pdata['name'])
        return HttpResponse(json.dumps('success'))
    
def getAll_view(request):
    # passPool=PasswordPool.objects.all()
    # print(passPool)
    # for item in passPool:
    #     print(item.username)
    #     print(item.password)
    #see if Justin is in our database
    # querylst=PasswordPool.objects.filter(username='kevin')
    # print(querylst)
    # if len(querylst)==0:
    #     print('Nothing in your database')
    # else:
    #     print('response is',querylst)
    # if u want to filter more items then add ,
    
    
    return HttpResponse('')
def hw2(request):
    Homeworkall=Homework2.objects.all()
    for item in Homeworkall:
        print(item.studentName,item.subject,item.score)
    Compare1=Homework2.objects.filter(subject='Math')
    Compare2=Homework2.objects.filter(subject='Physed')
    print(Compare1[0].score,Compare2[0].score)
    if Compare1[0].score>Compare2[0].score:
        print(Compare1[0].studentName+"'s", Compare1[0].subject,'score is higher than', Compare2[0].studentName+"'s", Compare2[0].subject,'score')
    else:
        print(Compare2[0].studentName+"'s", Compare2[0].subject,'score is higher than', Compare1[0].studentName+"'s", Compare1[0].subject,'score')
    
    return HttpResponse('')

def login_view(request):
    if request.method == 'POST':

        passPoolAll=PasswordPool.objects.all()
        test=json.loads(request.body.decode('utf-8'))
        user=test['user']
        pass1=test['pass']
        print(user)
        correctuser=PasswordPool.objects.filter(username=user,password=pass1)
        print(correctuser)
        if correctuser:
            print('The username',user,'is in the database')
            return HttpResponse(json.dumps({'msg':'correct'}))
        else:
            print('The username',user,'is not in the database')
            return HttpResponse(json.dumps({'msg':'incorrect'}))
    else:
        return HttpResponse(json.dumps('hello'))

def postblog_view(request):
    if request.method=='POST':
        retrieve=json.loads(request.body.decode('utf-8'))
        print(retrieve)
        return HttpResponse(json.dumps('Success'))
#homework
#table image in phone
#print out every student, obj and score
#two objects in obj, [math,english]. Who gets the highest score. SO basically we want to find who has the higheset score between two subjects

    
#notes: normally, we use two types request, one method is get, another is post
#get does not have a body, all request directly tupe in browser is get's request
#post request has a body

def hw1(request):
    if request.method=='POST':
        info=json.loads(request.body.decode('utf-8'))
        print(info)
        name1=info['name']
        course1=info['course']
        finalgrade1=info['finalgrade']
        FinalGrade.objects.create(name=name1,course=course1,finalgrade=finalgrade1)
        return HttpResponse(json.dumps('Success'))

    if request.method == 'GET':
        # get all data from our database
        objs = FinalGrade.objects.all()
        # convert our result to json type
        res = serializers.serialize('json',objs)
        return HttpResponse(res)