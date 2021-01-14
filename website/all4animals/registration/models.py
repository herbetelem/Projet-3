from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.
class User_data(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    # New fields
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    postal_code = models.IntegerField() 

    def __str__(self):
        return self.user

    class Meta:

        verbose_name = "User data"
        verbose_name_plural = "Données d'utilisateurs"
        ordering = ["user"]
