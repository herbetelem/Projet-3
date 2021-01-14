from django.contrib import admin
from django.urls import path
from . import views

app_name = "alert"

urlpatterns = [
    path('', views.index, name='index'),
    path('annonce/', views.Alert_view.as_view(), name='annonce'),
    path('annonce/<int:pk>/', views.Alert_detail.as_view(), name='choix_alert'),
    path('alerte/', views.alert, name='alerte'),
    path('contact/', views.contact, name='contact'),
]