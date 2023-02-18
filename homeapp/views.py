from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello World Django</h1>")

def bye(request):
    return HttpResponse("<h1>Bye World Django</h1>")

def hola(request):
    return HttpResponse("<h1>Hola World Django</h1>")
