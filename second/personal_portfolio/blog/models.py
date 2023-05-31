from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() #когда много текста
    date = models.DateField() #поле для работы с датой

    def __str__(self):
        return self.title
