from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'frontend/home.html')

def about(request):
    return render(request, 'frontend/about.html')

def factory(request):
    return render(request, 'frontend/factory.html')

def production(request):
    return render(request, 'frontend/production.html')

def dostavka(request):
    return render(request, 'frontend/dostavka.html')

def contacts(request):
    return render(request, 'frontend/contacts.html')

