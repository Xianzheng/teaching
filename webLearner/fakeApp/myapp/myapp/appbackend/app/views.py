from django.shortcuts import render
from django.http.response import HttpResponse
import json
# Create your views here.
def login(request):
    if request.method=='POST':
        return HttpResponse(json.dumps('Success'))
    return HttpResponse('hi')

def signUp(request):
    if request.method=='POST':
        return HttpResponse(json.dumps('success'))
    return HttpResponse('SignUp backend')

'''
1. create a UserDB in database, this table can show in admin,

2. signup can add user in userDB,

3. the length  of username is bigger than 5,
    the password must contain at least bigger letter, small letter, and the length is bigger than 8(you can use backend / front end)

4. after signup we can use this username and password to login

'''