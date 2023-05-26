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