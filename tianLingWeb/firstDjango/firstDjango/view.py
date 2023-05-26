from django.shortcuts import HttpResponse

def endpoint_view(request):
    return HttpResponse('<h1>Hello this is endpoint1</h1>')