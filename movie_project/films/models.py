from django.db import models

# Create your models here.
class Films_post(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    short_description = models.CharField('Краткое описание', max_length=200)
    text = models.TextField('Отзыв')

    def __str__(self):
        return self.title

