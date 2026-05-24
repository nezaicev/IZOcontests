from datetime import date
from django.db import models
from contests.utils import PathAndRename
from contests.directory import Material
from django.conf import settings
from ckeditor.fields import RichTextField
SIZE_CHOICES = [
    ('30x20', '30 × 20'),
    ('40x30', '40 × 30'),
    ('50x40', '50 × 40'),
    ('60x40', '60 × 40'),
    ('60x50', '60 × 50'),
    ('70x50', '70 × 50'),
    ('70x55', '70 × 55'),
    ('70x60', '70 × 60'),
    ('80x60', '80 × 60'),
    ('80x65', '80 × 65'),
    ('80x70', '80 × 70'),
    ('90x60', '90 × 60'),
    ('90x70', '90 × 70'),
    ('100x70', '100 × 70'),
    ('100x80', '100 × 80'),
    ('100x90', '100 × 90'),
    ('120x100', '120 × 100'),
    ('150x100', '150 × 100'),
    ('150x120', '150 × 120'),
]


# Create your models here.

def year_choices():
    return [(r, r) for r in range(1950, date.today().year + 1)]


class ProfileURAO(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    order=models.PositiveSmallIntegerField(
        verbose_name='Порядок',
        null=True,
    )

    avatar = models.ImageField(
        'Фото',
        upload_to='avatars/',
        blank=True,
        null=True
    )
    bio = RichTextField('О себе', blank=True)
    year_graduation = models.PositiveSmallIntegerField(
        choices=year_choices(),
        verbose_name='Год выпуска',
    blank = True,
    null = True
    )

    class Meta:
        ordering = ['order']
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'

    def __str__(self):
        return f'Профиль {self.user.email}'


class Image(models.Model):
    profile = models.ForeignKey(
        ProfileURAO,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Профиль',
        null=True,
        blank=True
    )
    author_name = models.CharField(max_length=150, blank=False,
                                   verbose_name='Авторское название')
    image = models.ImageField(upload_to=PathAndRename('urao/'),
                              max_length=200, verbose_name='Изображение')
    material = models.ForeignKey(Material, verbose_name='Материал',
                                 on_delete=models.SET_NULL, null=True)

    year = models.PositiveSmallIntegerField(
        choices=year_choices(),
        verbose_name='Год создания'
    )

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        verbose_name='Размер'
    )

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return str(self.author_name)
