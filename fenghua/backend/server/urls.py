from django.contrib import admin
from django.urls import path,include
from .views import first_view, second_view
urlpatterns = [
    path('',first_view),
    path('second/',second_view),
]