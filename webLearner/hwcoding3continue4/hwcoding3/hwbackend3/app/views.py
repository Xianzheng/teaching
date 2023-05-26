from ast import Pass
from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
import json
array=[]
def account(request):
    
    # if request.method=='POST':
    #     pdata=json.loads(request.body.decode('utf-8'))
    #     passarray=[]
    #     for i in pdata.keys():
    #         if i=='username1':
    #             passarray.append(pdata)
                
    #             for i in range(len(array)):
    #                 if passarray[0]['username1']==array[i]['username'] and passarray[0]['password1']==array[i]['password']:
    #                     print('It is the good password')
    #                     break
    #                 else:
    #                     continue  
    #             break
    #         else:
    #             array.append(pdata)
    #             break

            
    #     return HttpResponse(json.dumps(pdata))

    if request.method == 'POST':
        pdata=json.loads(request.body.decode('utf-8'))
        
        username = pdata['username']

        password = pdata['password']

        User.objects.create_user(username,password)
    # mod = User.objects.all()
    # User.objects.create_user('Kevin','a123')

    # mod = User.objects.all()
    # print(mod)
    
    return HttpResponse('Hello')

def login_view(request):

    if request.method == 'POST':
        loginData=json.loads(request.body.decode('utf-8'))
        loginUsername = loginData['username1']
        loginPassword = loginData['password1']

        print(loginUsername)
        print(loginPassword)
        
        check = User.objects.filter(username = loginUsername,
        password = loginPassword)

        """
        CRUD
        create
        retrieve
        update
        delete

        """

        print('check is',check)
        if check:
            print('valid')
        else:
            print('invalid')
    return HttpResponse('This is Login')




    
#next set up password pool in djajango, they help me to validate
# so login page
#if it is good password and username then send something to backend to print
#use margin-top('10px')
#margin left('10px')
#margin right('10px')
#the margins are demo to tell me to use demo ok future self. also use border 1px solid black
