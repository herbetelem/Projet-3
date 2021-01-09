from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_data(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # New fields
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    postal_code = models.IntegerField() 
    animal = models.ForeignKey('housing.Animal', on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return self.user

    class Meta:

        verbose_name = "User data"
        verbose_name_plural = "Données d'utilisateurs"
        ordering = ["user"]

