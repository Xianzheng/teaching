from django.contrib import admin
from django.urls import path
from .views import account, login_view

urlpatterns = [
    path('',account),
    path('login/',login_view),
]
