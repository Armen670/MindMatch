from django.contrib import admin
from django.urls import path
from .views import main

# ITS home urls file
urlpatterns = [
    path('', main, name='main'),
]
