from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from users.models import CustomUser


# Create your models here.


class Email(models.Model):
    date = models.DateTimeField(verbose_name='Дата создания', auto_now=True,
                                blank=True)
    theme = models.CharField(verbose_name='Тема', max_length=200,
                             blank=False, )
    content = RichTextField(verbose_name='Контент')
    user = models.ForeignKey(CustomUser, related_name='sender_email',
                             verbose_name='Пользователь',
                             on_delete=models.PROTECT)
    recipient = models.CharField(verbose_name='Получатель', max_length=20,
                                 blank=True, null=True)

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

    def __str__(self):
        return self.theme


class GroupSubscribe(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=200, blank=False)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группа'

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    MOSCOW = 'MSC'
    REGION = 'RG'
    REGION_CHOICES = [
        (MOSCOW, 'Москва и МО'),
        (REGION, 'Регион'),
    ]
    email = models.EmailField(_('email'), unique=True)
    group= models.ForeignKey(GroupSubscribe, verbose_name='Группа',
                             on_delete=models.PROTECT, null=True)
    phone_number = models.CharField(verbose_name='Телефон', max_length=15,
                                    blank=True,
                                    null=True)
    existing = models.BooleanField(verbose_name='Существование', default=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return self.email


class FileXls(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100,
                            default='Not name')
    file = models.FileField(verbose_name='Файл', upload_to='tmp/',
                            storage=FileSystemStorage)
    processed = models.BooleanField(verbose_name='Обработано', default=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name
