from django.urls import path
from Employee_management.APP1.views import *

urlpatterns = [

    path('',base ,name='base'),
    path('home/',home ,name='home'),
    path('about/',about ,name='about'),
    path('contact/',contact ,name='contact'),
]