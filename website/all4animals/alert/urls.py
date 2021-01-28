from django.contrib import admin
from django.urls import path
from . import views

app_name = "alert"

urlpatterns = [
    path('annonce_perdu/', views.alert_lost_view, name='lost'),
    path('annonce_trouver/', views.alert_find_view, name='find'),
    path('detail_annonce/<int:pk>/', views.Alert_detail.as_view(), name='detail_alert'),
    path('alerte/', views.alert, name='alerte'),
]