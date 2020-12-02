from django.db import models
from django.apps import apps


# User = apps.get_model('housing', 'User')
# Animal = apps.get_model('housing', 'Animal')
# Create your models here.



class Type_animal(models.Model):

    type = models.CharField(max_length=100)

    class Meta()


class Gender(models.Model):

    gender = models.CharField(max_length=100)
    

class Type_alert(models.Model):

    alert = models.CharField(max_length=100)

class Alert_user(models.Model):

    user = models.ForeignKey('housing.User_data', on_delete=models.CASCADE)
    animal = models.ForeignKey('housing.Animal', on_delete=models.CASCADE)
    type_alert = models.ForeignKey(Type_alert, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    type_animal = models.ForeignKey(Type_animal, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70)
    postal_code = models.IntegerField() 
    city = models.CharField(max_length=100)
    date = models.DateField()
    commentary = models.CharField(max_length=300)


