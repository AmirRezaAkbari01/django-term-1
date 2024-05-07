from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path('',index,name='index'),
    path('portfolio/',portfolio,name='portfolio'),
]
