from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from .managers import CustomAccountManager
from django.utils.translation import ugettext_lazy as _


class Position(models.Model):
    name = models.CharField('Должность', max_length=50, blank=False)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField('Регион', max_length=50, blank=False)

    def __str__(self):
        return self.name


class District(models.Model):
    name=models.CharField('Округ',max_length=10, blank=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name=models.CharField('Статус',max_length=15, blank=True)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    is_staff=models.BooleanField(default=False)
    email = models.EmailField(_('email'), unique=True)
    fio = models.CharField('ФИО', max_length=30, blank=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True)
    birth_date = models.DateField(null=True,blank=True)
    school = models.CharField('Образовательная организация', max_length=150, blank=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True,blank=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, null=True,blank=True)
    city = models.CharField('Населенный пункт', max_length=101, blank=True)
    phone = models.CharField('Телефон', max_length=15, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True,blank=True)

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
