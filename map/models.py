import os
import time
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django_selectel_storage.storage import SelectelStorage, Container
from map.utils import download_poster_video
# Create your models here.


class Placemark(models.Model):
    title=models.CharField(verbose_name='Заголовок',max_length=200)
    video_url=models.URLField(verbose_name='Видео')
    image_url = models.URLField(verbose_name='Изображение', blank=True)
    coordinates=ArrayField(models.FloatField(verbose_name='Координаты'), max_length=100)

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
        app_label = 'map'
        managed = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            self.set_poster_video()
        super(Placemark,self).save(*args, **kwargs)

    def set_poster_video(self):
        path_image=download_poster_video(self.video_url)
        storage = SelectelStorage()
        with open(path_image, 'rb') as image:
            selectel_img_url=storage._save(os.path.join('map',self.video_url.split('/')[-1]+'.png'), image.read())
        if storage.container.exists(selectel_img_url):
            self.image_url=storage.url(selectel_img_url)
        else:
            self.image_url=None




