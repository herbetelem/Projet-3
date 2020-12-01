from django.db import models
# from .alert.models import Type_animal
# from .alert.models import Gender

# # Create your models here.

# class User(models.Model):

#     pseudo = models.CharField(max_length=100)
#     email = models.EmailField(max_length=70)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=400)
#     postal_code = models.IntegerField() 
#     host = models.BooleanField() 

# class Housing_planning(models.Model):

#     id_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_type_animal = models.ForeignKey(Type_animal, on_delete=models.CASCADE)
#     number = models.IntegerField() 
#     start_date = models.DateField()
#     end_date = models.DateField()

# class Animal(models.Model):

#     name = models.CharField(max_length=100)
#     id_type_animal = models.ForeignKey(Type_animal, on_delete=models.CASCADE)
#     id_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
#     commentary = models.CharField(max_length=300)

# class housing_animal(models.Model):

#     id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
#     id_housing_planning = models.ForeignKey(Housing_planning, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     end_date = models.DateField()