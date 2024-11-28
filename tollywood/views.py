from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rebelstar(request):
    return HttpResponse('<h1>prabhas is acted by tollywood</h1>')

def megastar(request):
    return HttpResponse('<h1>chiranjeevi is acted by tollywood</h1>')

