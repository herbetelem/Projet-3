from django.shortcuts import render
from .models import Alert_user
from .forms import Alert_user_form

# Create your views here.

def index(request):
    return render(request, 'alert/index.html')

def contact(request):
    return render(request, 'alert/contact.html')


# Folder alert -----------------------------------------------------------
def alert_user(request):
    alert = Alert_user.objects.all()
    alert_user = {'alert_user': alert,}
    return render(request, 'alert/alert_user.html', alert_user)

def alert(request):
    form = Alert_user_form()
    if request.method == 'POST':
        form = Alert_user_form(request.POST)
        if form.is_valid() :
            form.save()

    context = {'form': form}
    return render(request, 'alert/create_alert.html', context)

def choice_alert(request):
    return render(request, 'alert/choice_alert.html')
