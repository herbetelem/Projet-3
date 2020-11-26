from django.db import models

# Create your models here.

# class User(models.Model):

#     pseudo = models.CharField(max_length=100)
#     email = models.EmailField(max_length=70)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     address = models.CharField(max_length=400)
#     postal_code = models.IntegerField() 
#     host = models.BooleanField() 

# class Type_animal(models.Model):

#     type = models.CharField(max_length=100)

    
# class Housing_planning(models.Model):

#     id_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_type_animal = models.ForeignKey(Type_animal, on_delete=models.CASCADE)
#     number = models.IntegerField() 
#     start_date = models.DateField()
#     end_date = models.DateField()


