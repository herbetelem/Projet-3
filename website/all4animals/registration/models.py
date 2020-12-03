from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_data(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # New fields
    address = models.CharField(max_length=300)
    postal_code = models.IntegerField() 

    def __str__(self):
        return User.username

    class Meta:

        verbose_name = "User data"
        verbose_name_plural = "Données d'utilisateurs"
        ordering = ["user"]

