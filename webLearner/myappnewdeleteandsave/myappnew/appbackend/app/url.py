from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    path('login/',login),
    path('signUp/',signUp),
    path('mainPage/',changepassMain),
    path('profile/',userprofile),
    path('getProfile/',getprofile),
    path('blogData/',blogdata),
    path('getBlog/',getBlog),
    path('bloginfo/',bloginfo),
    path('updateBlog/',updateBlog),
    path('deleteBlog/',deleteBlog)
]
