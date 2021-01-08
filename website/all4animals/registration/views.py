from django.shortcuts import render, redirect
from .registration import UserForm, UserDjango


# Create your views here.

def login(request):
    
    # traiter le requete post
    if request.method =="POST":
    # Instancier la classe formulaire, .save() pour enregistrer les données
        form = UserDjango(request.POST).save()
        # rediriger l'utilisateur
        return redirect('/index')
    else :
        form = UserDjango()
    return render(request, 'registration/login.html', {'form' : form} )