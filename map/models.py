from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Placemark(models.Model):
    title=models.CharField(verbose_name='Заголовок',max_length=200)
    video_url=models.URLField(verbose_name='Видео')
    image_url = models.URLField(verbose_name='Изображение')
    coordinates=ArrayField(models.FloatField(verbose_name='Координаты'))
