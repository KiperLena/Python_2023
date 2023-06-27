from django.db.models.signals import post_save, post_delete #сигнал уведомление
from django.dispatch import receiver #импорт декаратора
from django.contrib.auth.models import User #связь с юзерс
from .models import Profile #импорт класса профайл


@receiver(post_save, sender=User) #декаратор если сохраняем профиль пользователя
def create_profile(sender, instance, created, **kwargs):
    if created: #если создается новый пользователь, то
        user = instance #instance-имя пользователя сюда попадает
        profile = Profile.objects.create(
            user=user,
            username=user.username, #имена как в БД
            email=user.email,
            name=user.first_name,
        ) #создаем экземпляр модели. новый профиль пользователя

    # print('Profile Saved!')
    # print("Sender", sender)
    # print("Instance", instance)
    # print("Created", created)

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created is False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


    # print("Deleteing user ...")


# post_save.connect(profile_update, sender=Profile)
# post_delete.connect(delete_user, sender=Profile)












