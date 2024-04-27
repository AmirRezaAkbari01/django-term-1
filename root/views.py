from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'root/index.html')


def contact(request):
    return render(request,'root/contact.html')

def about(request):
    return render(request,'root/about.html')

def Game(request):
    return render(request,'root/Game.html')