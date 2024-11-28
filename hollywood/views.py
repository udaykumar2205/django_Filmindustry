from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def actionking(request):
    return HttpResponse('<h1>Robertdowny is acted by hollywood</h1>')

def marvelking(request):
    return HttpResponse('<h1>steverogers is acted by hollywood</h1>')
