from django.db import models
from django.contrib.auth.models import User



# Type_animal = apps.get_model('alert', 'Type_animal')
# Gender = apps.get_model('alert', 'Gender')

# Create your models here.

# class User(models.Model):

#     pseudo = models.CharField(max_length=100)
#     email = models.EmailField(max_length=70)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=400)
#     postal_code = models.IntegerField() 
#     host = models.BooleanField() 

class User_data(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # New fields
    address = models.CharField(max_length=300)
    postal_code = models.IntegerField() 

    def __str__(self):
        return f'{User.username}'


class Housing_planning(models.Model):

    user = models.ForeignKey(User_data, on_delete=models.CASCADE)
    type_animal = models.ForeignKey('alert.Type_animal', on_delete=models.CASCADE)
    number = models.IntegerField() 
    start_date = models.DateField()
    end_date = models.DateField()

class Animal(models.Model):

    name = models.CharField(max_length=100)
    type_animal = models.ForeignKey('alert.Type_animal', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.ForeignKey('alert.Gender', on_delete=models.CASCADE)
    commentary = models.CharField(max_length=300)

class Housing_animal(models.Model):

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    housing_planning = models.ForeignKey(Housing_planning, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()