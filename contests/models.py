import time
import os
from uuid import uuid4
from django.db import models
from django.utils.deconstruct import deconstructible
from model_utils.managers import InheritanceManager
from users.models import CustomUser, Region, District
from contests import utils


# Create your models here.

class Nomination(models.Model):
    name = models.CharField('Номинация', max_length=100)

    class Meta:
        verbose_name = 'Номинация'
        verbose_name_plural = 'Номинация'

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField('Класс', max_length=10)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField('Материал', max_length=50)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материал'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField('Статус', max_length=35, blank=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

    def __str__(self):
        return self.name


class BaseContest(models.Model):
    objects = InheritanceManager()
    reg_number = models.CharField(max_length=15, blank=False, null=False,
                                  unique=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fio = models.CharField('ФИО участника', max_length=40)
    school = models.CharField('Образовательная организация', max_length=150)
    city = models.CharField('Город', max_length=101, blank=True)
    year_contest = models.CharField('Год проведения', max_length=20,
                                    default=utils.generate_year())
    status = models.ForeignKey(Status, verbose_name='Статус',
                               on_delete=models.PROTECT, null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name='Регион',
                               on_delete=models.PROTECT, null=True)
    date_reg = models.DateTimeField(auto_now=True, blank=True)
    district = models.ForeignKey(District, verbose_name='Округ',
                                 on_delete=models.PROTECT, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.reg_number = int(time.time())
        super(BaseContest, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.reg_number)


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance:
            # Задаем имя файла по маске
            filename = '{}.{}'.format(instance.reg_number, ext)
        else:
            # иначе генерируем по хэшу
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


class Artakiada(BaseContest):
    full_name = 'АРТакиада "Изображение и слово"'
    name = 'АРТакиада "Изображение и слово"'
    alias = 'artakiada'
    image = models.ImageField(upload_to=PathAndRename('artakiada/'),
                              max_length=100, verbose_name='Изображение')
    material = models.ForeignKey(Material, verbose_name='Материал',
                                 on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, verbose_name='Класс',
                              on_delete=models.SET_NULL, null=True)
    nomination = models.ForeignKey(Nomination, verbose_name='Номинация',
                                   on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.reg_number)

    class Meta:
        verbose_name = 'АРТакиада (участник)'
        verbose_name_plural = 'АРТакиада (участники)'


class NRusheva(BaseContest):
    theme = models.CharField(max_length=50, blank=True)


class Mymoskvichi(BaseContest):
    full_name = 'Конкурс мультимедиа "Мы Москвичи"'
