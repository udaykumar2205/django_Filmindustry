from django.urls import path
from bollywood.views import *

urlpatterns=[
    path('bigstar/',bigstar,name='bigstar'),
    path('stylishstar/',stylishstar,name='stylishstar'),
]