from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required #декоратор



def home(request):
    return render(request, 'salut/home.html')

def registeruser(request):
    if request.method == 'GET':
        return render(request, 'salut/registeruser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('curentsalut')
            except IntegrityError:
                return render(request, 'salut/registeruser.html', {'form': UserCreationForm(),
                                                                'error': 'Такое имя пользователя уже существует. Задайте другое.'})
        else:
            return render(request, 'salut/registeruser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


@login_required
def curentsalut(request):
    return render(request, 'salut/curentsalut.html')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'salut/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'salut/loginuser.html', {'form': AuthenticationForm(), 'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('curentsalut')

@login_required
def usasalut(request):
    return render(request, 'salut/usasalut.html')

@login_required
def francesalut(request):
    return render(request, 'salut/francesalut.html')







