from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.


class Page(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Псевдоним')
    title = models.CharField(verbose_name='Заголовок', max_length=400)
    subtitle = models.CharField(verbose_name='Подзаголовок', max_length=400)
    content = RichTextUploadingField(verbose_name='Контент')

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.slug
