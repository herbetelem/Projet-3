from django.contrib import admin
from .models import User_data
from .models import Housing_planning
from .models import Animal
from .models import Housing_animal

# Register your models here.

admin.site.register(User_data)
admin.site.register(Housing_planning)
admin.site.register(Animal)
admin.site.register(Housing_animal)