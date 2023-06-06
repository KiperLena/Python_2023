from django.forms import ModelForm
from .models import Todo



class TodoForm(ModelForm):
    class Meta:  #служебный класс из ModelForm
        model = Todo #с какоймоделью делаем связь поля
        fields = ['title', 'memo', 'important'] #какие поля выводить



























