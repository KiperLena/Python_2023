from django.forms import ModelForm #импорт формы чтобы поля правильно обрабатывались
from django import forms
from .models import Project #импорт проекта


class ProjectForm(ModelForm): #класс наследуется от модел форм
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags' ] #какие поля выводим в виде формы
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        } #меняем тип данных в строке заполнения

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input'})
        # self.fields['description'].widget.attrs.update({'class': 'input'})
        # self.fields['demo_link'].widget.attrs.update({'class': 'input'})
        # self.fields['source_link'].widget.attrs.update({'class': 'input'})
