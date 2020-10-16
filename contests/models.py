import time
from django.db import models
from model_utils.managers import InheritanceManager
from users.models import CustomUser
from contests import utils
# Create your models here.


class Status(models.Model):
    name=models.CharField('Статус',max_length=10)

    def __str__(self):
        return self.name


class Region(models.Model):
    name=models.CharField('Регион',max_length=25)

    def __str__(self):
        return self.name


class District(models.Model):
    name=models.CharField('Округ',max_length=10)

    def __str__(self):
        return self.name


class BaseContest(models.Model):
    objects=InheritanceManager()
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    reg_number = models.CharField(max_length=15, blank=False, null=False, unique=True)
    date_reg = models.DateTimeField(auto_now=True, blank=True)
    school = models.CharField('Образовательная организация', max_length=150, blank=True)
    fio = models.CharField('ФИО участника', max_length=40, blank=True)
    city = models.CharField('Город', max_length=101, blank=True)
    year_contest = models.CharField('Год проведения',max_length=20, default=utils.generate_year())
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.reg_number = int(time.time())
        super(BaseContest, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.reg_number)


class Artakiada(BaseContest):
    info=models.CharField(max_length=50,blank=True)


class NRusheva(BaseContest):
    theme=models.CharField(max_length=50,blank=True)