from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
def about(request):
    return render(request, 'generator/about.html')

def password(request):
    return render(request, 'generator/password.html')
