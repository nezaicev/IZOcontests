import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import JSONField
from django.core.files.storage import FileSystemStorage
from contests.models import Status


# Create your models here.

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


class Font(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название шрифта')
    url = models.FileField(upload_to='fonts/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шрифт'
        verbose_name_plural = 'Шрифты'


class Text(models.Model):
    name = models.CharField(verbose_name='Название поля', max_length=50,
                            default='Title')
    LINE = [('ma', 'ma'), ('mt', 'mt'), ('mm', 'mm'),
            ('mb', 'mb'), ('md', 'md'), ('rs', 'rs'),
            ('ls', 'ls'), ('ms', 'ms')]
    ALIGN = [('center', 'center'),
             ('left', 'left'),
             ('right', 'right')
             ]

    size = models.IntegerField(verbose_name='Размер шрифта', default=50)
    color = models.CharField(verbose_name='Цвет текста', default='#000000',
                             max_length=7)
    position = JSONField(verbose_name='Позиция', default=list)
    font = models.ForeignKey(Font, verbose_name='Шрифт',
                             on_delete=models.PROTECT)
    anchor = models.CharField(choices=LINE, default='ms', max_length=5)
    width = models.IntegerField(verbose_name='Длинна текста', default=50)
    align = models.CharField(verbose_name='Выравнивание текста', choices=ALIGN,
                             default='center', max_length=10)
    offset=models.IntegerField(verbose_name='Отступ (низ)', default=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текст'


class Cert(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(
                "Max file size is %sMB" % str(megabyte_limit))

    blank = models.ImageField(storage=FileSystemStorage,
                              verbose_name='Бланк сертификата',
                              upload_to='certs/', blank=False,
                              validators=[validate_image]
                              )
    access = models.BooleanField(verbose_name='Доступ', default=False)
    contest = models.ForeignKey(Events, verbose_name='Конкурс', max_length=15,
                                blank=False, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, verbose_name='Статус участника',
                               blank=False,
                               on_delete=models.PROTECT)
    fio_text = models.ForeignKey(Text, related_name='fio', verbose_name='ФИО',
                                 on_delete=models.PROTECT)
    reg_num_text = models.ForeignKey(Text, related_name='reg_num',
                                     verbose_name='Регистрационный номер',
                                     on_delete=models.PROTECT)
    position_text = models.ForeignKey(Text, related_name='status',
                                    verbose_name='Должность/класс',
                                    on_delete=models.PROTECT,
                                    )

    school_text = models.ForeignKey(Text, related_name='school',
                                    verbose_name='Организация',
                                    on_delete=models.PROTECT, null=True,
                                    blank=True)
    nomination_text = models.ForeignKey(Text, related_name='nomination',
                                        verbose_name='Номинация',
                                        on_delete=models.PROTECT, blank=True,
                                        null=True)
    article=models.CharField(verbose_name='Артикул', max_length=7,
                             default=str(datetime.datetime.now().year)[2:]
                             )

    def __str__(self):
        return "Сертификат {} {}".format(self.contest.name, self.status)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
