from django.contrib import admin
from .models import Type_animal
from .models import Gender
from .models import Type_alert
from .models import Alert_user

# Register your models here.

admin.site.register(Type_animal)
admin.site.register(Gender)
admin.site.register(Type_alert)
admin.site.register(Alert_user)