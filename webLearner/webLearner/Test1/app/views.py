from django.shortcuts import render

from django.http.response import HttpResponse

# Create your views here.
def hello_view(request):
    # return HttpResponse("Hello World")
    lst = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    return render(request,'hello.html',{'data':lst})

