from django.contrib import admin
from django.urls import path
from .views import *
app_name='post'

urlpatterns = [
    path('about/',about,name='about'),
    #path('contact/',contact,name='contact'),
    path('form/',contact,name='contact'),
    path('brand/',brand,name='brand'),
    path('index/',index,name='index'),
    path('special/',special,name='special'),

]
