from django.contrib import admin
from django.urls import path

from django.urls import re_path
from firstapp import views
 
urlpatterns = [
   
    path('', views.index),
    
]
