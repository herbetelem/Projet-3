from django.forms import ModelForm
from .models import Alert_user

class Alert_user_form(ModelForm):
    class Meta:
        model = Alert_user
        fields = '__all__'
