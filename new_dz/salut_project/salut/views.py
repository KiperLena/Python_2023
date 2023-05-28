from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Salut! Елена Анатольевна, django в PyCharm так и не заработал, работаю через командную строку")