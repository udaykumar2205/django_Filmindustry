from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bigstar(request):
    return HttpResponse('<h1>salmankhan is acted by bollywood</h1>')

def stylishstar(request):
    return HttpResponse('<h1>sharukkhan is acted by bollywood</h1>')