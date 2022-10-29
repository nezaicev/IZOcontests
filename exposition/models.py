from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from contests.models import CROP_ORIENTATION
from contests.utils import PathAndRename


class Exposition(models.Model):
    title = models.CharField(verbose_name='Название', max_length=300)
    poster = models.ImageField(verbose_name='Афиша',
                               upload_to=PathAndRename('exposition/posters/'))
    address = models.CharField(verbose_name='Адрес проведения', max_length=300)
    content = RichTextField(verbose_name='Контент')
    start_date = models.DateField(verbose_name='Начало экспонирования')
    end_date = models.DateField(verbose_name='Конец экспонирования')
    archive = models.BooleanField(verbose_name='Архив', default=False)
    count_exp = models.IntegerField(verbose_name='Количество едениц')
    count_participants = models.IntegerField(
        verbose_name='Количество участников')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date', ]
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'


class ImageExposition(models.Model):
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=PathAndRename(
                                  'exposition/images'))
    images = models.ForeignKey(Exposition,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True, related_name='images')
    order_number = models.IntegerField(verbose_name='Порядковый номер',
                                       null=True, blank=True)
    crop_orientation_img = models.CharField(max_length=50,
                                            verbose_name='Ориентация превью',
                                            choices=CROP_ORIENTATION,
                                            default='center',
                                            )

    class Meta:
        ordering = ['order_number', ]
        verbose_name = 'Изображение (Выставка)'
        verbose_name_plural = 'Изображения для выставки'

    @property
    def image_tag(self):
        if self.images:
            return mark_safe(
                '<img src="{}" width="100px" height="100px" />'.format(
                    get_thumbnail(self.image, '300x300', crop='center',
                                  quality=99).url
                ))
        else:
            return ''




