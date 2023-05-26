from django.shortcuts import render
from django.http.response import HttpResponse
import json
# Create your views here.

def first_view(request):
    return HttpResponse('<h1>Today is a happy day</h1>')

def second_view(request):
    res = json.dumps('this is second view')
    return HttpResponse(res)

# 练习 建立服务器的全过程

# 多写几遍fetch

# 让前后端交互

