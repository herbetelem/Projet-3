from django.shortcuts import render, redirect
from .registration import UserForm, UserDjango
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, CustomerForm

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:
        user = None
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('../')
        
        else:
            messages.info(request, 'Username OR password is incorrect')
        
        return render(request, 'registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('../')
    else:
        form = CreateUserForm()
        
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')


        context = {'form':form,}
        return render(request, 'registration/register.html', context)

@login_required(login_url='login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'registration/account_settings.html', context)