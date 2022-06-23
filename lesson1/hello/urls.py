<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>",views.message, name="message")
=======
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:name>",views.message, name="message")
>>>>>>> 5ea0922c35e5667ea76b239636d07a5241cb41d7
]