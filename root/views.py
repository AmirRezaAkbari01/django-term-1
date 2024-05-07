from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'root/index.html')

def portfolio(request):
    return render(request,'root/portfolio-details.html')
