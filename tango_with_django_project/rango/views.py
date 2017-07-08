from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says her there partner!<br/><a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rangso says here is the about page.<br/>Back to <a href='/rango/'>index</a>")
