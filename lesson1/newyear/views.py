<<<<<<< HEAD
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", 
=======
from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", 
>>>>>>> 5ea0922c35e5667ea76b239636d07a5241cb41d7
        {"newyear": now.month == 1 and now.day==1})