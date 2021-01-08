from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('annonce/', views.alert_user, name='annonce'),
    path('alerte/', views.alert, name='alerte'),
    path('choix_alert/', views.choice_alert, name='choix_alert'),
]