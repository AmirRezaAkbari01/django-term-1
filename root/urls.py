from django.http import HttpResponse
from django.urls import path
from .views import *




urlpatterns=[
    path('',home),
    path('contact/',contact),
    path('about/',about),
    path('game/',Game),
    path('date/',date),
]