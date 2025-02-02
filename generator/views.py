from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'gbdhcjs4348r53ds'})

def index(request):
    return HttpResponse('This is the index page')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : thepassword})

def about(request):
    return render(request, 'generator/about.html')