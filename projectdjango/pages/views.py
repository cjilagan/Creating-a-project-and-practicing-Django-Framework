from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def signup_view(request, *args, **kwargs):
    return HttpResponse("<h1>Signup Page</h1>")