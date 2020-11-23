from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')

def hebergement(request):
    return render(request, 'mysite/hebergement.html')