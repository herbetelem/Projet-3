"""all4animals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hebergement/', views.housing, name='hebergement'),
    path('profil/', views.profil, name='profil'),
    path('annonce/', views.browse_ad, name='annonce'),
    path('alerte/', views.alert, name='alerte'),
    path('mon_calendrier/', views.my_calendar, name='mon_calendrier'),
    path('calendrier_user/', views.user_calendar, name='calendrier_user'),
    path('recherche_hebergement/', views.housing_search, name='recherche_hebergement'),
    path('se_connecter/', views.login, name='se_connecter'),

]
