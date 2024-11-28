from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def thalapathy(request):
    return HttpResponse('<h1>vijay is acted by kollywood</h1>')

def superstar(request):
    return HttpResponse('<h1>Rajini kanth  is acted by kollywood </h1>')