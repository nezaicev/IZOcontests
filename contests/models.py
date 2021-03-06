import time
import os
from uuid import uuid4
from django.db import models
from django.utils.deconstruct import deconstructible
from django.conf import settings
from model_utils.managers import InheritanceManager
from ckeditor.fields import RichTextField
from users.models import CustomUser, Region, District
from contests import utils


# Create your models here.
class Age(models.Model):
    name = models.CharField('Возраст', max_length=10)

    class Meta:
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возраст'

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField('Тема', max_length=60)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


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
    fields = None
    objects = InheritanceManager()
    reg_number = models.CharField(max_length=20, blank=False, null=False,
                                  unique=True,
                                  verbose_name='Регистрационный номер')
    barcode=models.CharField(verbose_name='Штрих-код',max_length=15,blank=False,null=False)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fio = models.CharField('Участник', max_length=40)
    fio_teacher = models.CharField('ФИО педагога', max_length=40)
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
                                 on_delete=models.PROTECT, null=True,
                                 blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.reg_number = str(int(time.time())) + str(
                CustomUser.objects.get(email=self.teacher).id)
            self.barcode=self.reg_number[6:]
        super(BaseContest, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    def get_fields_for_pdf(self, attrs_obj=None):
        if not attrs_obj:
            attrs_obj = []
            attrs_obj.append(self.name)
        for attr in self.fields:
            if type(getattr(self, attr)) is str:
                field_value = getattr(self, attr)
            elif getattr(self, attr) is None:
                continue
            else:
                field_value = getattr(self, attr).name
            attrs_obj.append((getattr(self.__class__, attr).field.verbose_name,
                              field_value))
        if self.teacher:
            attrs_obj.append((self.teacher.__class__.fio.field.verbose_name,
                              self.teacher.fio))
            attrs_obj.append((self.teacher.__class__.email.field.verbose_name,
                              self.teacher.email))
        return tuple(attrs_obj)

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
            if hasattr(instance, 'reg_number'):
                filename = '{}.{}'.format(instance.reg_number, ext)
            else:
                filename = '{}.{}'.format(int(time.time()), ext)

        else:
            # иначе генерируем по хэшу
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


class Artakiada(BaseContest):
    fields = (
    'year_contest', 'reg_number', 'fio','fio_teacher', 'school', 'level', 'region', 'city',
    'district', 'nomination', 'material',)
    full_name = 'АРТакиада "Изображение и слово"'
    name = ('Конкурс', 'АРТакиада "Изображение и слово"')
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
    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school', 'level',
        'age','region', 'city','district', 'theme', 'material','author_name',
        'format','description'
    )
    full_name = 'Конкурс им. Нади Рушевой'
    name = ('Конкурс', 'Конкурс им. Нади Рушевой')
    alias = 'nrusheva'

    theme = models.ForeignKey(Theme, verbose_name='Тема',
                                   on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, verbose_name='Класс',
                              on_delete=models.SET_NULL, null=True)
    age = models.ForeignKey(Age, verbose_name='Возраст',
                              on_delete=models.SET_NULL, null=True)

    image = models.ImageField(upload_to=PathAndRename('nrusheva/'),
                              max_length=100, verbose_name='Изображение')
    material = models.ForeignKey(Material, verbose_name='Материал',
                                 on_delete=models.SET_NULL, null=True)
    author_name = models.CharField(max_length=50, blank=False,
                                   verbose_name='Авторское название')
    format = models.CharField(max_length=2, choices=(('A1','A1'),('A2','A2'),('A3','A3')), blank=False,
                              verbose_name='Формат работы')
    description = models.TextField(max_length=500, blank=False,
                                   verbose_name='Аннотация')

    def __str__(self):
        return str(self.reg_number)

    class Meta:
        verbose_name = 'Конкурс им. Нади Рушевой (участник)'
        verbose_name_plural = 'Конкурс им. Нади Рушевой (участники)'


class Mymoskvichi(BaseContest):
    full_name = 'Конкурс мультимедиа "Мы Москвичи"'


class PageContest(models.Model):
    name = models.CharField(verbose_name='Название конкурса', max_length=150,
                            blank=True)
    logo = models.ImageField(verbose_name='Логотип',
                             upload_to=PathAndRename('PageContests/'))
    content = RichTextField(verbose_name='Контент')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Страница конкурса'
        verbose_name_plural = 'Страницы конкурсов'
