from django.contrib import admin
from django.urls import path
from .views import getAll_view, hello, hw2, login_view
from .views import postData_view
from .views import postblog_view
from .views import hw1
urlpatterns = [
    path('hi/',hello),
    path('postData/',postData_view),
    path('getAll/',getAll_view),
    path('hw2/',hw2),
    path('',login_view),
    path('postblog/',postblog_view),
    path('finalgrade/',hw1)
]

