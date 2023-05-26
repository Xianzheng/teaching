from django.contrib import admin
from django.urls import path
from .views import login
from .views import signUp
urlpatterns = [
    path('login/',login),
    path('signUp/',signUp)
    
]
