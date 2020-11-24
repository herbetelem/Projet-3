from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')




# Folder profil ----------------------------------------------------------
def profil(request):
    return render(request, 'mysite/profil/profil.html')

def login(request):
    return render(request, 'mysite/profil/login.html')


def my_calendar(request):
    return render(request, 'mysite/profil/my_calendar.html')


# Folder alert -----------------------------------------------------------
def browse_ad(request):
    return render(request, 'mysite/alert/browse_ad.html')

def alert(request):
    return render(request, 'mysite/alert/alert.html')


# Folder hounsing---------------------------------------------------------
def housing(request):
    return render(request, 'mysite/housing/housing.html')

def user_calendar(request):
    return render(request, 'mysite/housing/user_calendar.html')

def housing_search(request):
    return render(request, 'mysite/housing/housing_search.html')
