from django.shortcuts import render
from .models import Skills

def index(request):
    projects = Skills.objects.all() #получение данных из БД
    return render(request, 'skills/index.html', {'projects': projects})

