from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'alert/index.html')

def contact(request):
    return render(request, 'alert/contact.html')


# Folder alert -----------------------------------------------------------
def browse_ad(request):
    return render(request, 'alert/browse_ad.html')

def alert(request):
    return render(request, 'alert/alert.html')
