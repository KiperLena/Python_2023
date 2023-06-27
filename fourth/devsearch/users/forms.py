from django.contrib.auth.forms import UserCreationForm #импорт форма создания пользователя
from django.contrib.auth.models import User #откуда будет выгружать из формы
from .models import Profile, Skill
from django.forms import ModelForm


class SkillForm(ModelForm): #для коррекции скиллов
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class ProfileForm(ModelForm): #для коррекции профиля
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'short_info', 'profile_image',
                  'social_github', 'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class CustomUserCreationForm(UserCreationForm): #наследуемся от стандартного модуля форм
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Name'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})









