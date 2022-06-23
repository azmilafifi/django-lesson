<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")


def message(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!!")

def greet(request,name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
=======
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")


def message(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!!")

def greet(request,name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
>>>>>>> 5ea0922c35e5667ea76b239636d07a5241cb41d7
    })