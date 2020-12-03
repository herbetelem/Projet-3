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
from alert import views
from housing import views as housing_views
from registration import views as registration_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profil/', housing_views.profil, name='profil'),
    path('login/', registration_views.login, name='login'),
    path('annonce/', views.browse_ad, name='annonce'),
    path('alerte/', views.alert, name='alerte'),
    path('mon_calendrier/', housing_views.my_calendar, name='mon_calendrier'),
    path('calendrier_user/', housing_views.user_calendar, name='calendrier_user'),
    path('recherche_hebergement/', housing_views.housing_search, name='recherche_hebergement'),
    path('hebergement/', housing_views.housing, name='hebergement'),
    path('contact/', views.contact, name='contact'),
    path('choix_alert/', views.choice_alert, name='choix_alert'),

]
