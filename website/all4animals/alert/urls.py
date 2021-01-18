from django.contrib import admin
from django.urls import path
from . import views

app_name = "alert"

urlpatterns = [
    path('', views.index, name='index'),
    path('annonce_perdu/', views.alert_lost_view, name='annonce'),
    path('annonce_trouver/', views.Alert_find_view.as_view(), name='trouver'),
    path('detail_annonce/<int:pk>/', views.Alert_detail.as_view(), name='choix_alert'),
    path('alerte/', views.alert, name='alerte'),
]