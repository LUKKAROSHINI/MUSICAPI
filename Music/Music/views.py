from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def register(request):
    return render(request, "register.html")

def adminhome(request):
    return render(request, "adminhome.html")
def billing(request):
    return render(request, "billing.html")