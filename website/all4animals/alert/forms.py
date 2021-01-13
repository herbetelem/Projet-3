from django.forms import ModelForm
from .models import Alert_user

class Create_user_form(ModelForm):
    class Meta:
        model = Alert_user
        fields = '__all__'
