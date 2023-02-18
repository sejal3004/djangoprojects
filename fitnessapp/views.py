from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def legday(request):
    return HttpResponse("<h1>Today is legday</h1><br></br><h2>Dont break a leg!!!</h2>")


def cardio(request):
    return HttpResponse("<h1>Today is cardio day</h1><br></br><h2>One step at a time!</h2>")



