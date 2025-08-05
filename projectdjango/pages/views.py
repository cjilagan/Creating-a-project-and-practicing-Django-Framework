from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def signup_view(request, *args, **kwargs):
    return HttpResponse("<h1>Signup Page</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about us",
        "my_number": 9916957243,
        "my_list": [1321, 23213, 3321, 4412, 5123],
    }
    return render(request, "about.html", my_context)