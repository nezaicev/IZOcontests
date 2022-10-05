import time

from django.db import models

from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

from users.models import CustomUser
from contests.utils import PathAndRename
from contests.directory import Status
from cert.models import Cert


class Event(models.Model):
    TYPE_CONTESTS = (
        ('Мероприятие', 'Мероприятие'),
        ('Анонс', 'Анонс'))
    name = models.CharField(verbose_name='Название мероприятия',
                            max_length=350,
                            blank=False)
    type = models.CharField(verbose_name='Тип',
                            choices=TYPE_CONTESTS,
                            default='Мероприятие', max_length=20)
    start_date = models.DateTimeField(verbose_name='Начало мероприятия',
                                      blank=True, null=True)
    logo = models.ImageField(verbose_name='Изображение',
                             upload_to=PathAndRename('PageContests/'),
                             blank=True, null=True)
    message = models.TextField(verbose_name='Информация', blank=True, null=True)
    send_letter = models.BooleanField(default=False,
                                      verbose_name='Отправить письмо')
    letter = RichTextField(verbose_name='Письмо', blank=True, null=True)
    certificate = models.ForeignKey(Cert, verbose_name='Сертификат',
                                    on_delete=models.PROTECT, null=True,
                                    blank=True)
    hide = models.BooleanField(verbose_name='Скрыть', default=False)
    broadcast_url=models.URLField(verbose_name='Трансляция', blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.start_date.date())

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class ParticipantEvent(models.Model):

    reg_number = models.CharField(max_length=20, blank=False, null=False,
                                  unique=True,
                                  verbose_name='Регистрационный номер')
    event = models.ForeignKey(Event, on_delete=models.PROTECT,
                              verbose_name='Мероприятие', max_length=300)

    participant = models.ForeignKey(CustomUser, verbose_name='Участник',
                                    null=False, on_delete=models.CASCADE)
    date_reg = models.DateTimeField(verbose_name='Дата регистрации',
                                    auto_now=True)
    status = models.ForeignKey(Status, verbose_name='Статус участника',
                               on_delete=models.PROTECT, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.reg_number = str(int(time.time())) + str(self.participant.id)
        super(ParticipantEvent, self).save(*args, **kwargs)

    def certificate(self):
        if self.event.certificate:
            return mark_safe(
                '<a target="_blank" href="/certs/confirmation/event/?reg_number={}">Сертификат</a>'.format(
                    self.reg_number)
            )
        else:
            return '-'

    def __str__(self):
        return '{}'.format(self.participant.fio)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        permissions = [
            ("export_participants", "Выгрузить список участников"),
        ]
        unique_together = ('participant', 'event',)