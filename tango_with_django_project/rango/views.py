from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says her there partner!<br/><a href='/rango/about/'>About</a>")

def about(request):
    return render(request, 'rango/about.html')
    #return HttpResponse("Rangso says here is the about page.<br/>Back to <a href='/rango/'>index</a>")
