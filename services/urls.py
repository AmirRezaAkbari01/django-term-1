from django . urls import path
from .views import *


app_name='services'

urlpatterns = [
    path('',services,name='services'),
    path('services-detail/',services_detail,name='services-detail'),
    path('qoute/',qoute,name='qoute')
]
