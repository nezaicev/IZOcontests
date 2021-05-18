from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.


class Subscriber(models.Model):
    MOSCOW = 'MSC'
    REGION='RG'
    REGION_CHOICES = [
        (MOSCOW, 'Москва и МО'),
        (REGION, 'Регион'),
    ]
    email = models.EmailField(verbose_name='Email', unique=True)
    region = models.CharField(verbose_name='Регион', max_length=10,
                              default=MOSCOW, choices=REGION_CHOICES)
    phone_number = models.CharField(verbose_name='Телефон', max_length=15, blank=True,
                             null=True)
    existing = models.BooleanField(verbose_name='Существование', default=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return self.email


class FileXls(models.Model):
    name=models.CharField(verbose_name='Название',max_length=100, default='Not name')
    file=models.FileField(verbose_name='Файл', upload_to='tmp/', storage=FileSystemStorage)
    processed=models.BooleanField(verbose_name='Обработано',default=True)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name
