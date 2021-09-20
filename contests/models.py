import time
import os
from uuid import uuid4
from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.safestring import mark_safe
from model_utils.managers import InheritanceManager
from ckeditor.fields import RichTextField
from users.models import CustomUser, Region, District
from contests import utils
from contests.directory import NominationART, NominationMYMSK, ThemeART, \
    ThemeRUSH, ThemeMYMSK, AgeRUSH, AgeMYMSK, Status, Level, Material


# Create your models here.
# Заявки на конкурсы


class Events(models.Model):
    name = models.CharField(verbose_name='Название (конкурс/мероприятие)',
                            max_length=100, blank=False)
    app = models.CharField(verbose_name='Приложение', max_length=30,
                           blank=False)
    model = models.CharField(verbose_name='Модель', max_length=30, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Select(models.Model):
    field = models.CharField('Название поля', max_length=20,
                             choices=(
                                 ('nomination', 'Номинация'),
                                 ('age', 'Возраст'),
                                 ('theme', 'Тема')))
    data = models.CharField('Данные', max_length=500)

    class Meta:
        abstract = True
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return self.data


class BaseContest(models.Model):
    fields = None
    objects = InheritanceManager()
    reg_number = models.CharField(max_length=20, blank=False, null=False,
                                  unique=True,
                                  verbose_name='Регистрационный номер')
    barcode = models.CharField(verbose_name='Штрих-код', max_length=15,
                               blank=False, null=False)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fio = models.CharField('Участник', max_length=300)
    fio_teacher = models.CharField('Педагог', max_length=300)
    school = models.CharField('Образовательная организация', max_length=150)
    city = models.CharField('Город', max_length=101, blank=True)
    year_contest = models.CharField('Год проведения', max_length=20,
                                    default=utils.generate_year())
    status = models.ForeignKey(Status, verbose_name='Статус',
                               on_delete=models.PROTECT, null=True, default=3)
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
            self.barcode = self.reg_number[6:]
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
        if instance:
            if hasattr(instance, 'reg_number'):
                filename = '{}.{}'.format(instance.reg_number, ext)
            else:
                filename = '{}.{}'.format(int(time.time()), ext)

        else:
            filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


class ShowEvent(BaseContest):
    back_email = 'cnho@yandex.ru'
    fields = None
    full_name = 'Мероприятие'
    name = ('Мероприятие', '')
    alias = 'event'

    page_contest = models.ForeignKey('PageContest', verbose_name='Мероприятие',
                                     on_delete=models.CASCADE)

    def save(self, *args, **kwargs):

        self.fio = self.teacher.fio
        self.fio_teacher = self.teacher.fio
        self.school = self.teacher.school
        self.city = self.city
        self.region = self.teacher.region
        self.district = self.teacher.district
        super(ShowEvent, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Публичное мероприятие'
        verbose_name_plural = 'Публичные мероприятия'


class Artakiada(BaseContest):
    back_email = 'artakiada@mioo.ru'
    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school', 'level',
        'region', 'city',
        'district', 'nomination', 'material',)
    full_name = 'АРТакиада "Изображение и слово"'
    name = ('Конкурс', 'АРТакиада "Изображение и слово"')
    alias = 'artakiada'
    image = models.ImageField(upload_to=PathAndRename('artakiada/'),
                              max_length=200, verbose_name='Изображение')
    material = models.ForeignKey(Material, verbose_name='Материал',
                                 on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, verbose_name='Класс',
                              on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(ThemeART, verbose_name='Тема',
                              on_delete=models.SET_NULL, null=True, blank=True)
    nomination = models.ForeignKey(NominationART, verbose_name='Номинация',
                                   on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.reg_number)

    def image_tag(self):
        if self.image:
            return mark_safe(
                '<a data-fancybox="gallery" data-caption="{}, {}, {}" href="{}" class="image-link">Изображение</a>'.format(
                    self.reg_number, self.fio, self.level, self.image.url))
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'АРТакиада (участник)'
        verbose_name_plural = 'АРТакиада (участники)'


class NRusheva(BaseContest):
    back_email = 'nrusheva@mioo.ru'
    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school', 'level',
        'age', 'region', 'city', 'district', 'theme', 'material',
        'author_name',
        'format', 'description'
    )
    full_name = 'Конкурс им. Нади Рушевой'
    name = ('Конкурс', 'Конкурс им. Нади Рушевой')
    alias = 'nrusheva'

    theme = models.ForeignKey(ThemeRUSH, verbose_name='Тема',
                              on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, verbose_name='Класс',
                              on_delete=models.SET_NULL, null=True)
    age = models.ForeignKey(AgeRUSH, verbose_name='Возраст',
                            on_delete=models.SET_NULL, null=True)

    image = models.ImageField(upload_to=PathAndRename('nrusheva/'),
                              max_length=200, verbose_name='Изображение')
    material = models.ForeignKey(Material, verbose_name='Материал',
                                 on_delete=models.SET_NULL, null=True)
    author_name = models.CharField(max_length=50, blank=False,
                                   verbose_name='Авторское название')
    format = models.CharField(max_length=2, choices=(
        ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3')), blank=False,
                              verbose_name='Формат работы')
    description = models.TextField(max_length=500, blank=False,
                                   verbose_name='Аннотация')

    def __str__(self):
        return str(self.reg_number)

    def image_tag(self):
        if self.image:
            return mark_safe(
                '<a data-fancybox="gallery" data-caption="{}, {}, {}" href="{}" class="image-link">Изображение</a>'.format(
                    self.reg_number, self.fio, self.age, self.image.url)
            )
        else:
            return 'No Image Found'

    class Meta:
        verbose_name = 'Конкурс им. Нади Рушевой (участник)'
        verbose_name_plural = 'Конкурс им. Нади Рушевой (участники)'


class Mymoskvichi(BaseContest):
    full_name = 'Конкурс мультимедиа "Мы Москвичи"'
    name = ('Конкурс', 'Конкурс мультимедиа Мы Москвичи')
    alias = 'mymoskvichi'
    back_email = 'mymoskvichi@mioo.ru'
    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school',
        'region', 'city', 'district', 'age', 'author_name', 'nomination',
        'nomination_extra', 'program',
    )
    nomination = models.ForeignKey(NominationMYMSK, verbose_name='Номинация',
                                   on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(ThemeMYMSK, verbose_name='Тема',
                              on_delete=models.SET_NULL, null=True)

    author_name = models.CharField(max_length=50, blank=False,
                                   verbose_name='Авторское название')
    program = models.CharField(max_length=100, blank=False,
                               verbose_name="Программа(ы), в которой выполнена работа",
                               null=True)
    age = models.ForeignKey(AgeMYMSK,
                            verbose_name='Возрастная категория',
                            null=True, on_delete=models.SET_NULL)
    link = models.CharField(max_length=200,
                            verbose_name='Ссылка на файл (облако)',
                            null=True)

    def __str__(self):
        return str(self.reg_number)

    class Meta:
        verbose_name = 'Конкурс Мы Москвичи (участники)'
        verbose_name_plural = 'Конкурс Мы Москвичи (участники)'

    def generate_list_participants(self, model, fios=None):
        if fios == None:
            fios = ''
            participants = list(
                model.objects.filter(participants_id=self.pk).values_list(
                    'fio', flat=True))
            for participant in participants:
                if participant != participants[-1]:
                    fios += participant + ', '
                else:
                    fios += participant
            return fios


class Participant(models.Model):
    fio = models.CharField(max_length=50, verbose_name='Фамилия, имя',
                           blank=False)
    participants = models.ForeignKey(Mymoskvichi, verbose_name='Участники',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class TeacherExtra(models.Model):
    fio = models.CharField(max_length=50, verbose_name='ФИО', blank=False)
    participants = models.ForeignKey(Mymoskvichi, verbose_name='Педагог',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'


class PageContest(models.Model):
    name = models.CharField(verbose_name='Название конкурса', max_length=150,
                            blank=True)
    start_date = models.DateTimeField(verbose_name='Начало мероприятия',
                                      blank=True, null=True)
    logo = models.ImageField(verbose_name='Логотип',
                             upload_to=PathAndRename('PageContests/'),
                             blank=True, null=True)
    content = RichTextField(verbose_name='Контент', blank=True, null=True)
    type = models.CharField(verbose_name='Тип',
                            choices=(('1', 'Конкурс'), ('2', 'Мероприятие'), ('3', 'Анонс')),
                            default=1, max_length=20)
    letter = RichTextField(verbose_name='Письмо', blank=True, null=True)
    hide = models.BooleanField(verbose_name='Скрыть', default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Страница мероприятия'
        verbose_name_plural = 'Страницы мероприятия'


class Message(models.Model):
    name = models.CharField(verbose_name='Заголовок', blank=True,
                            max_length=100)
    content = RichTextField(verbose_name='Контент')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class ModxDbimgMuz(models.Model):
    location = models.CharField(db_column='Location', max_length=255,
                                blank=True, null=True)
    oldname = models.CharField(db_column='oldName', max_length=255, blank=True,
                               null=True)
    dateupload = models.CharField(db_column='dateUpload', max_length=255,
                                  blank=True, null=True)
    competition1 = models.CharField(max_length=255, blank=True, null=True)
    picturename = models.CharField(db_column='PictureName', max_length=255,
                                   blank=True, null=True)
    material = models.CharField(db_column='Material', max_length=255,
                                blank=True, null=True)
    fiocompetitor = models.CharField(db_column='FioCompetitor', max_length=255,
                                     blank=True, null=True)
    agecompetitor = models.CharField(db_column='ageCompetitor', max_length=255,
                                     blank=True, null=True)
    age = models.IntegerField(db_column='Age', blank=True, null=True)
    shcoolname = models.CharField(db_column='shcoolName', max_length=255,
                                  blank=True, null=True)
    fioteacher = models.CharField(db_column='FioTeacher', max_length=255,
                                  blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    temaname = models.CharField(db_column='TemaName', max_length=255,
                                blank=True, null=True)
    quarter = models.IntegerField(blank=True, null=True)
    sortage = models.IntegerField(db_column='sortAge', blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=255, blank=True,
                              null=True)
    cityname = models.CharField(db_column='cityName', max_length=255,
                                blank=True, null=True)
    pathfile = models.CharField(db_column='pathFile', max_length=255)
    hesh = models.CharField(max_length=255, blank=True, null=True)
    available = models.CharField(db_column='Available', max_length=255,
                                 blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modx_dbimg_muz'


class Archive(BaseContest):
    date_reg = models.DateTimeField(blank=True)
    contest_name = models.CharField(max_length=200, null=False,
                                    verbose_name='Конкурс', blank=False)
    year_contest = models.CharField('Год проведения', max_length=20,
                                    blank=False, null=False)
    image = models.ImageField(upload_to=PathAndRename('all_contests/'),
                              max_length=200, verbose_name='Изображение',
                              blank=True, null=True)
    material = models.ForeignKey(Material, verbose_name='Материал',
                                 on_delete=models.SET_NULL, null=True,
                                 blank=True)
    level = models.ForeignKey(Level, verbose_name='Класс',
                              on_delete=models.SET_NULL, null=True, blank=True)
    theme = models.CharField(verbose_name='Тема',
                             max_length=200, null=True, blank=True)
    nomination = models.CharField(verbose_name='Номинация',
                                  max_length=200, null=True, blank=True)

    age = models.CharField(verbose_name='Возраст',
                           max_length=50, null=True, blank=True)

    author_name = models.CharField(max_length=50, blank=True, null=True,
                                   verbose_name='Авторское название',
                                   )
    format = models.CharField(max_length=2, choices=(
        ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3')), blank=True, null=True,
                              verbose_name='Формат работы')
    description = models.TextField(max_length=500, blank=True, null=True,
                                   verbose_name='Аннотация')

    program = models.CharField(max_length=100, blank=True, null=True,
                               verbose_name="Программа(ы), в которой выполнена работа",
                               )
    link = models.CharField(max_length=200,
                            blank=True, verbose_name='Ссылка на файл (облако)',
                            null=True)

    city = models.CharField('Город', max_length=101, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(BaseContest, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Архив'
        verbose_name_plural = 'Архив'

    def __str__(self):
        return self.reg_number
