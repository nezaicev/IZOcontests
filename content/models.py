import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from contests.utils import PathAndRename

unique_id = uuid.uuid4().hex


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
    section = models.CharField('Раздел', max_length=255, blank=False, null=False)
    order = models.IntegerField('Порядковый номер', null=True, blank=True, default=1)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.order = self.pk
        super(Video, self).save(*args, **kwargs)

    class Meta:
        ordering = ('order',)
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
    title = models.CharField('Название', max_length=100)
    link = models.URLField('Ссылка', max_length=400)
    poster = models.ImageField(verbose_name='Обложка',
                               upload_to=PathAndRename('publication/posters/'))
    order = models.IntegerField('Порядковый номер')
    year = models.CharField('Год', max_length=10,
                            choices=(('2024', '2024'), ('2023', '2023'), ('2022', '2022'),
                                     ('2021', '2021'), ('2020', '2020'), ('2019', '2019'),
                                     ('2018', '2018'), ('2017', '2017'), ('2016', '2016'),
                                     ('2015', '2015'), ('2014', '2014'), ('2013', '2013'),
                                     ('2012', '2012'), ('2011', '2011'), ('2010', '2010')))

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Publication, self).save(*args, **kwargs)
            self.order = self.pk
        super(Publication, self).save(*args, **kwargs)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
