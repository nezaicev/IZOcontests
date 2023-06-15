import os
import random
import time

from django.conf import settings
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
from model_utils.managers import InheritanceManager
from ckeditor.fields import RichTextField
from sorl.thumbnail import get_thumbnail

import contests.directory

from contests.utils import PathAndRename
from users.models import CustomUser, Region, District, Status as StatusTeacher

from contests import utils
from contests.directory import NominationART, NominationMYMSK, ThemeART, \
    ThemeRUSH, ThemeMYMSK, AgeRUSH, AgeMYMSK, Status, Level, Material, \
    NominationVP, AgeVP, LevelVP, NominationNR, DirectionVP, AgeART
from contests.validators import validate_file_extension
from phonenumber_field.modelfields import PhoneNumberField


class PageContest(models.Model):
    TYPE_CONTESTS = {'1': 'Конкурс',
                     '2': 'Мероприятие',
                     '3': 'Анонс'}
    alias = models.CharField(verbose_name='Псевдоним', blank=False,
                             max_length=100, default='test')

    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    name = models.CharField(verbose_name='Название конкурса',
                            max_length=250, default='test',
                            blank=True)
    start_date = models.DateTimeField(verbose_name='Начало',
                                      blank=True, null=True)
    logo = models.ImageField(verbose_name='Логотип',
                             upload_to=PathAndRename('PageContests/'),
                             blank=True, null=True)
    content = RichTextField(verbose_name='Контент', blank=True, null=True)
    # type = models.CharField(verbose_name='Тип',
    #                         choices=(('1', 'Конкурс'), ('2', 'Мероприятие'),
    #                                  ('3', 'Анонс')),
    #                         default=1, max_length=20)
    letter = RichTextField(verbose_name='Письмо', blank=True, null=True)
    hide = models.BooleanField(verbose_name='Скрыть кнопку перехода', default=False)
    order = models.IntegerField(verbose_name='Порядковый номер', default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Страница конкурса'
        verbose_name_plural = 'Страницы конкурсов'


def get_info_contests(alias_contest):
    try:
        pc = PageContest.objects.get(alias=alias_contest)
        return pc.pk
    except ObjectDoesNotExist:
        print(
            'Необходимо создать "Страницу мероприятия" с псевдонимом {}'.format(
                alias_contest))


class Events(models.Model):
    name = models.CharField(verbose_name='Название (конкурс/мероприятие)',
                            max_length=100, blank=False)
    event = models.ForeignKey('PageContest', verbose_name='Мероприятие',
                              blank=True, null=True,
                              on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Мероприятия для сертификатов'


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
    objects = InheritanceManager()
    info = models.ForeignKey('PageContest', verbose_name='Информация',
                             blank=False, on_delete=models.PROTECT, null=True)
    reg_number = models.CharField(max_length=20, blank=False, null=False,
                                  unique=True,
                                  verbose_name='Регистрационный номер')
    barcode = models.CharField(verbose_name='Штрих-код', max_length=15,
                               blank=False, null=False)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fio = models.CharField('Участник', max_length=5000)
    fio_teacher = models.CharField('Педагог', max_length=300)
    school = models.CharField('Образовательная организация', max_length=150)
    city = models.CharField('Город', max_length=101)
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
    email = models.EmailField(verbose_name='Электронная почта', null=True)
    status_change = models.BooleanField(verbose_name='Статус изменения',
                                        default=False)

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
            attrs_obj.append(
                ('Конкурс', self.info.name))
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
                              CustomUser.objects.get(id=self.teacher_id).fio))
            attrs_obj.append((self.teacher.__class__.email.field.verbose_name,
                              self.teacher.email))
        return tuple(attrs_obj)

    @classmethod
    def get_stat_data(cls):
        id_status_teacher = StatusTeacher.objects.get(name='Педагог').id
        id_status_statement_error = Status.objects.get(name='Ошибка').id

        result = {
            'statement_count': cls.objects.all().exclude(status=id_status_statement_error).count(),
            'teacher_count': cls.objects.select_related('teacher__status').filter(
                teacher__status=id_status_teacher).values(
                'teacher_id').distinct().count(),
            'school_count': cls.objects.values('school').distinct().count(),
            'region_count': cls.objects.all().exclude(status=id_status_statement_error).values(
                'region').distinct().count(),
            'participant_count': cls.objects.all().exclude(
                status=id_status_statement_error).count(),
        }
        return result

    def __str__(self):
        return str(self.reg_number)


class ShowEvent(BaseContest):
    fields = None
    page_contest = models.ForeignKey('PageContest',
                                     related_name='page_contest_show_event',
                                     verbose_name='Мероприятие',
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
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        permissions = [
            ("export_participants", "Выгрузить список участников"),
        ]


class Artakiada(BaseContest):
    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school', 'level',
        'age',
        'region', 'city',
        'district', 'nomination', 'material', 'author_name')
    author_name = models.CharField(max_length=50, blank=False,
                                   verbose_name='Авторское название')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True,
                                null=True,
                                )
    age = models.ForeignKey(AgeART, verbose_name='Возраст',
                            on_delete=models.SET_NULL, null=True)
    info = models.ForeignKey('PageContest', on_delete=models.SET_NULL,
                             null=True, default=get_info_contests('artakiada'))

    image = models.ImageField(upload_to=PathAndRename('artakiada/'),
                              max_length=200, verbose_name='Изображение')
    material = models.ForeignKey(Material, verbose_name='Материал',
                                 on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, verbose_name='Класс',
                              on_delete=models.SET_NULL, null=True)
    theme = models.ForeignKey(ThemeART, verbose_name='Тема',
                              on_delete=models.SET_NULL, null=True)
    nomination = models.ForeignKey(NominationART, verbose_name='Номинация',
                                   on_delete=models.SET_NULL, null=True)

    snils_gir = models.CharField(max_length=20, verbose_name='СНИЛС',
                                 null=True, blank=True)
    phone_gir = models.CharField(verbose_name='Контактный телефон', null=True,
                                 blank=True, max_length=50)
    address_school_gir = models.CharField(verbose_name='Адрес организации',
                                          null=True, blank=True,
                                          max_length=200)

    def __str__(self):
        return str(self.reg_number)

    def image_tag(self):
        if self.image:
            context = {
                'reg_number': self.reg_number,
                'fio': self.fio,
                'age': self.age,
                'image_url': self.image.url,
                'thumb_image': get_thumbnail(self.image.url, '75x75',
                                             crop='center', quality=99).url,
                'icon_url': "/static/site/img/rotate.svg",
                'api_url': 'http://{}/contests/api/rotate_image_artakiada/'.format(
                    os.getenv('HOSTNAME'))
            }

            return mark_safe(

                render_to_string('buttons/rotate_image.html', context=context)

            )
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'АРТакиада (участник)'
        verbose_name_plural = 'АРТакиада (участники)'


class NRusheva(BaseContest):
    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school', 'level',
        'age', 'region', 'city', 'district', 'theme', 'material',
        'author_name',
        'format', 'description',
        'nomination',
    )
    info = models.ForeignKey('PageContest', on_delete=models.SET_NULL,
                             null=True, default=get_info_contests('nrusheva'))

    theme = models.ForeignKey(ThemeRUSH, verbose_name='Тема',
                              on_delete=models.SET_NULL, null=True)
    nomination = models.ForeignKey(NominationNR, verbose_name='Номинация',
                                   on_delete=models.SET_NULL, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True,
                                null=True,
                                )
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

    snils_gir = models.CharField(max_length=20, verbose_name='СНИЛС',
                                 null=True, blank=True)
    phone_gir = models.CharField(verbose_name='Контактный телефон', null=True,
                                 blank=True, max_length=50)
    address_school_gir = models.CharField(verbose_name='Адрес организации',
                                          null=True, blank=True,
                                          max_length=200)

    def __str__(self):
        return str(self.reg_number)

    def image_tag(self):
        if self.image:
            context = {
                'reg_number': self.reg_number,
                'fio': self.fio,
                'age': self.age,
                'image_url': self.image.url,
                'thumb_image': get_thumbnail(self.image.url, '75x75',
                                             crop='center', quality=99).url,

                'api_url': 'http://{}/contests/api/rotate_image_nrusheva/'.format(
                    os.getenv('HOSTNAME'))
            }

            return mark_safe(

                render_to_string('buttons/rotate_image.html', context=context)

            )
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'Конкурс им. Нади Рушевой (участник)'
        verbose_name_plural = 'Конкурс им. Нади Рушевой (участники)'


class MultiParticipants:

    def generate_list_participants(self, model, filed='fio', enumeration=None):
        if enumeration is None:
            enumeration = ''
            participants = utils.generate_enumeration_field_by_id(self.id,
                                                                  model, filed)
            for item in participants:
                if item != participants[-1]:
                    enumeration += item + ', '
                else:
                    enumeration += item
            return enumeration


class VP(BaseContest, MultiParticipants):
    INDIVIDUAL = '1'
    COLLECTIVE = '2'
    LESSON = '3'
    DIRECTION = [
        (INDIVIDUAL, 'Индивидуальный проект'),
        (COLLECTIVE, 'Коллективный проект'),
        (LESSON, 'Урочный проект')
    ]

    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school',
        'region', 'city', 'district', 'author_name', 'nomination',
        'direction', 'ovz',
    )
    info = models.ForeignKey('PageContest', on_delete=models.SET_NULL,
                             null=True, default=get_info_contests('vp'))
    author_name = models.CharField(max_length=200, blank=False,
                                   verbose_name='Авторское название')
    direction = models.ForeignKey(DirectionVP, on_delete=models.SET_NULL,
                                  verbose_name='Форма организации', null=True)

    nomination = models.ForeignKey(NominationVP, verbose_name='Номинация',
                                   on_delete=models.SET_NULL, null=True)
    level = models.ManyToManyField(LevelVP, related_name='levels',
                                   verbose_name='Класс',
                                   )
    ovz = models.CharField(verbose_name='Проект, выполнен детьми с ОВЗ',
                           blank=False, default='Нет',
                           choices=(('Нет', 'Нет'), ('Да', 'Да')),
                           max_length=10)
    phone_gir = models.CharField(verbose_name='Контактный телефон', null=True,
                                 blank=True, max_length=50)

    def __str__(self):
        return str(self.reg_number)

    class Meta:
        verbose_name = 'Конкурс Художественных проектов (участники)'
        verbose_name_plural = 'Конкурс Художественных проектов (участники)'
        permissions = [
            ("export_participants", "Выгрузить список участников"),
        ]

    @classmethod
    def get_stat_data(cls):
        stat = super().get_stat_data()
        id_status_statement_error = Status.objects.get(name='Ошибка').id
        stat['participant_count'] = ParticipantVP.objects.select_related(
            'participants__status').all().exclude(
            participants__status=id_status_statement_error).count()
        stat['teacher_count'] = TeacherExtraVP.objects.select_related(
            'participants__status').all().exclude(
            participants__status=id_status_statement_error).count()

        return stat

    def get_fields_for_pdf(self, attrs_obj=None):
        list_fields = list(super().get_fields_for_pdf())
        list_fields.append((self.teacher.__class__.phone.field.verbose_name,
                            CustomUser.objects.get(id=self.teacher_id).phone))

        value_level = str([item[0] for item in
                           self.level.values_list('name')]).replace("'",
                                                                    '').replace(
            "]", '').replace("[", '')
        list_fields.append(('Класс',
                            value_level))

        return tuple(list_fields)


class ParticipantVP(models.Model):
    fio = models.CharField(max_length=50, verbose_name='Фамилия, имя, отчество',
                           blank=False)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True,
                                null=True,
                                )
    level = models.CharField(max_length=30, verbose_name='Класс',
                             blank=True, null=True)
    snils_gir = models.CharField(max_length=20, verbose_name='СНИЛС',
                                 null=True, blank=True)
    participants = models.ForeignKey(VP, verbose_name='Участники',
                                     on_delete=models.CASCADE)


    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class TeacherExtraVP(models.Model):
    fio = models.CharField(max_length=50, verbose_name='ФИО', blank=False)
    participants = models.ForeignKey(VP, verbose_name='Педагог',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'


class Mymoskvichi(BaseContest, MultiParticipants):
    fields = (
        'year_contest', 'reg_number', 'fio', 'fio_teacher', 'school',
        'region', 'city', 'district', 'age', 'author_name', 'nomination',
        'program',
    )
    info = models.ForeignKey('PageContest', on_delete=models.SET_NULL,
                             null=True,
                             default=get_info_contests('mymoskvichi'))

    nomination = models.ForeignKey(NominationMYMSK, verbose_name='Номинация',
                                   on_delete=models.SET_NULL, null=True)

    author_name = models.CharField(max_length=700, blank=False,
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

    phone_gir = PhoneNumberField(verbose_name='Контактный телефон', null=True,
                                 default='+7'
                                 )
    address_school_gir = models.CharField(verbose_name='Адрес организации',
                                          null=True, blank=True,
                                          max_length=200)
    duration = models.CharField(verbose_name='Длительность', default='3:30',
                                max_length=100, null=True)

    description_file = models.FileField(upload_to=PathAndRename('file/'),
                                        validators=[validate_file_extension],
                                        max_length=200,
                                        verbose_name='Описание и сценарий',
                                        null=True
                                        )
    ovz = models.CharField(verbose_name='Проект, выполнен детьми с ОВЗ',
                           blank=False, default='Нет',
                           choices=(('Нет', 'Нет'), ('Да', 'Да')),
                           max_length=10)

    def __str__(self):
        return str(self.reg_number)

    class Meta:
        verbose_name = 'Конкурс Мы Москвичи (участники)'
        verbose_name_plural = 'Конкурс Мы Москвичи (участники)'

    @classmethod
    def get_stat_data(cls):
        stat = super().get_stat_data()

        id_status_statement_error = Status.objects.get(name='Ошибка').id
        stat['participant_count'] = ParticipantMymoskvichi.objects.select_related(
            'participants__status').all().exclude(
            participants__status=id_status_statement_error).count()
        stat['teacher_count'] = TeacherExtraMymoskvichi.objects.select_related(
            'participants__status').all().exclude(
            participants__status=id_status_statement_error).count()

        return stat


class ParticipantMymoskvichi(models.Model):
    fio = models.CharField(max_length=50, verbose_name='Фамилия Имя Отчество',
                           blank=False)
    participants = models.ForeignKey(Mymoskvichi, verbose_name='Участники',
                                     on_delete=models.CASCADE)
    birthday = models.DateField(verbose_name='Дата Рождения', blank=True,
                                null=True

                                )
    snils_gir = models.CharField(max_length=20, verbose_name='СНИЛС',
                                 null=True, blank=True)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = 'Участник (Мы Москвичи)'
        verbose_name_plural = 'Участники (Мы Москвичи)'


class TeacherExtraMymoskvichi(models.Model):
    fio = models.CharField(max_length=50, verbose_name='ФИО', blank=False)
    participants = models.ForeignKey(Mymoskvichi, verbose_name='Педагог',
                                     on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fio)

    class Meta:
        verbose_name = 'Педагог (Мы Москвичи)'
        verbose_name_plural = 'Педагоги (Мы Москвичи)'


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


from cert.models import Cert

CROP_ORIENTATION = (('top', 'Верх'),
                    ('center', 'Центр'),
                    ('bottom', 'Низ'),
                    ('left', 'Лево'),
                    ('right', 'Право'))

CONTESTS_NAME = (('Дизайн детям', 'Дизайн детям'),)


class Archive(models.Model):
    reg_number = models.CharField(max_length=20, blank=False, null=False,
                                  unique=True,
                                  verbose_name='Регистрационный номер')
    barcode = models.CharField(verbose_name='Штрих-код', max_length=15,
                               blank=False, null=False)

    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                blank=True, null=True)
    fio = models.CharField('Участник', max_length=5000, blank=True, null=True,
                           default='')
    fio_teacher = models.CharField('Педагог', max_length=300, blank=True,
                                   null=True)
    school = models.CharField('Образовательная организация', max_length=150,
                              blank=True, null=True)
    city = models.CharField('Город', max_length=101, blank=True, null=True)
    year_contest = models.CharField('Год проведения', max_length=20,
                                    blank=True, null=True)
    status = models.ForeignKey(Status, verbose_name='Статус',
                               on_delete=models.PROTECT, null=True, default=1)
    region = models.ForeignKey(Region, verbose_name='Регион',
                               on_delete=models.PROTECT, blank=True, null=True)
    date_reg = models.DateTimeField(blank=True, null=True)
    district = models.ForeignKey(District, verbose_name='Округ',
                                 on_delete=models.PROTECT, null=True,
                                 blank=True)

    rating = models.FloatField('Рейтинг', default=0)
    publish = models.BooleanField(verbose_name='Опубликовать', default=False)
    contest_name = models.CharField(max_length=200,
                                    null=True,
                                    verbose_name='Конкурс', blank=True)
    image = models.ImageField(upload_to=PathAndRename('all_contests/'),
                              max_length=200, verbose_name='Изображение',
                              blank=True, null=True)
    crop_orientation_img = models.CharField(max_length=50,
                                            verbose_name='Ориентация превью',
                                            choices=CROP_ORIENTATION,
                                            default='center',
                                            )
    material = models.CharField(max_length=200, verbose_name='Материал',
                                null=True,
                                blank=True)
    level = models.CharField(max_length=200, verbose_name='Класс',
                             null=True, blank=True)
    theme = models.CharField(verbose_name='Тема',
                             max_length=200, null=True, blank=True)
    nomination = models.CharField(verbose_name='Номинация',
                                  max_length=200, null=True, blank=True)
    direction = models.CharField(verbose_name='Направление',
                                 max_length=200, null=True, blank=True)

    age = models.CharField(verbose_name='Возраст',
                           max_length=50, null=True, blank=True)

    author_name = models.CharField(max_length=250, blank=True, null=True,
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

    participants = models.IntegerField(verbose_name='participants', blank=True,
                                       null=True)

    def save(self, *args, **kwargs):
        if self.reg_number == '':
            self.reg_number = '{}-{}'.format(round(random.random()*10000),str(int(time.time())))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Архив'
        verbose_name_plural = 'Архив'
        ordering = ['-rating', 'reg_number']

        indexes = [
            models.Index(fields=['contest_name', 'nomination', '-rating']),

        ]

    def __str__(self):
        return self.reg_number

    def certificate(self):
        try:
            contest = Events.objects.get(
                event=PageContest.objects.get(name=self.contest_name).id)
            blank = Cert.objects.get(contest=contest.id, status=self.status,
                                     year_contest=self.year_contest)
            if blank:
                return mark_safe(
                    '<a target="_blank" href="/certs/?reg_number={}&event={}">Сертификат</a>'.format(
                        self.reg_number, contest.id)
                )
            else:
                return '-'
        except ObjectDoesNotExist:
            return '-'


class ExtraImage(models.Model):
    image = models.ImageField(upload_to=PathAndRename('all_contests/'),
                              max_length=200, verbose_name='Изображение',
                              blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.image.url)


class ExtraImageVP(ExtraImage):
    extra_images = models.ForeignKey(VP, verbose_name='Изображения',
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE,
                                     related_name='images',
                                     )

    def __str__(self):
        return str(self.image)

    @property
    def image_tag(self):
        if self.image:
            return mark_safe(

                '<a data-fancybox="gallery" id="{}_img" href = "{}" class ="image-link"> <img src="{}" width="100px" height="100px" /></a>'.format(
                    self.id,
                    self.image.url,
                    get_thumbnail(self.image, '300x300', crop='center', quality=99).url
                ))
        else:
            return ''

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'


class ExtraImageArchive(ExtraImage):
    extra_images = models.ForeignKey(Archive,
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
        verbose_name = 'Изображения архив'
        verbose_name_plural = 'Изображения архив'

    @property
    def image_tag(self):
        if self.extra_images:
            return mark_safe(
                '<img src="{}" width="100px" height="100px" />'.format(
                    get_thumbnail(self.image, '300x300', crop='center',
                                  quality=99).url
                ))
        else:
            return ''


class Video(models.Model):
    name = models.CharField(verbose_name='Название', max_length=300)
    video = models.URLField(
        max_length=200, verbose_name='Ссылка',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.video)


class VideoVP(Video):
    videos = models.ForeignKey(VP, verbose_name='Видео',
                               blank=True,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='videos',
                               )

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class VideoArchive(Video):
    videos = models.ForeignKey(Archive,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True, related_name='videos')
    order_number = models.IntegerField(verbose_name='Порядковый номер',
                                       null=True, blank=True)

    class Meta:
        ordering = ['order_number', ]
        verbose_name = 'Видео архив'
        verbose_name_plural = 'Видео архив'


class File(models.Model):
    name = models.CharField(verbose_name='Название', max_length=300)
    file = models.FileField(upload_to=PathAndRename('file/'),
                            validators=[validate_file_extension],
                            max_length=200, verbose_name='Файл', )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class FileArchive(File):
    files = models.ForeignKey(Archive,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True, related_name='files')

    class Meta:
        verbose_name = 'Файлы архив'
        verbose_name_plural = 'Файлы архив'


class FileVP(File):
    files = models.ForeignKey(VP,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True, related_name='files')

    class Meta:
        verbose_name = 'Файлы (Аннотация|Презентация)'
        verbose_name_plural = 'Файлы (Аннотация|Презентация)'


class CreativeTack(models.Model):
    contest_name = models.CharField('Конкурс', max_length=50)
    year_contest = models.CharField('Год', max_length=50)
    theme = models.CharField('Тема|Номинация', max_length=200)
    content = RichTextField(verbose_name='Контент')

    class Meta:
        unique_together = ['contest_name', 'year_contest', 'theme']
        verbose_name = 'Творческое задание'
        verbose_name_plural = 'Творческие задания'

    def __str__(self):
        return f"{self.theme} {self.contest_name} {self.year_contest}"
