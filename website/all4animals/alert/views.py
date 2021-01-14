from django.shortcuts import render
from django.views import generic
from .models import Alert_user
from .forms import Create_alert

# Create your views here.

def index(request):
    return render(request, 'alert/index.html')

def contact(request):
    return render(request, 'alert/contact.html')


# Folder alert -----------------------------------------------------------
# def alert_user(request):
#     alert = Alert_user.objects.all()
#     alert_user = {'alert_user': alert,}
#     return render(request, 'alert/alert_user.html', alert_user)



class Alert_view(generic.ListView):

    template_name = "alert/alert_user.html"
    context_object_name = "alert_user"


    def get_queryset(self):
        alert_user = Alert_user.objects.all()
        return alert_user

class Alert_detail(generic.DetailView):

    model = Alert_user
    template_name = "alert/alert_detail.html"
    
def alert(request):
    form = Create_alert()
    if request.method == 'POST':
        form = Create_alert(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
        print()
        print(f"erreur = {form.errors}")

    context = {'form': form}
    return render(request, 'alert/create_alert.html', context)


def choice_alert(request):
    return render(request, 'alert/choice_alert.html')

