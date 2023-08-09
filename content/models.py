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


class Video(models.Model):
    title = models.CharField('Название', max_length=200, null=False, blank=False)
    description = models.CharField('Описание', max_length=300, null=True, blank=True)
    link = models.URLField('Ссылка', blank=False, null=False)
    categories = models.ManyToManyField('Category', related_name='categories',
                                        verbose_name='Категория', )
    order = models.IntegerField('Порядковый номер', default=1)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('Название', max_length=100, blank=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Publication(models.Model):
    pass
