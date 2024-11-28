from django.urls import path
from tollywood.views import *

urlpatterns=[
    path('rebelstar/',rebelstar,name='rebelstar'),
    path('megastar/',megastar,name='megastar'),
]