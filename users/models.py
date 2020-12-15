from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,Group
from django.db import models
from .managers import CustomAccountManager
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _


class Position(models.Model):
    name = models.CharField('Должность', max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField('Регион', max_length=50, blank=False)
    
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField('Округ', max_length=10, blank=True)
    
    class Meta:
        verbose_name = 'Округ'
        verbose_name_plural = 'Округа'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField('Статус', max_length=35, blank=True)
    
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Age(models.Model):
    name = models.CharField('Возрастная категория', max_length=15, blank=True)
    
    class Meta:
        verbose_name = 'Возрастная катеогия'
        verbose_name_plural = 'Возрастная категория'

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    default_group_teacher='Teacher'
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(_('email'), unique=True)
    fio = models.CharField(verbose_name='ФИО пользователя', max_length=30)
    school = models.CharField('Образовательная организация', max_length=150, )
    region = models.ForeignKey(Region, verbose_name='Регион',
                               on_delete=models.SET_NULL, default=1,null=True)
    district = models.ForeignKey(District, verbose_name='Округ',
                                 on_delete=models.SET_NULL, null=True,
                                 blank=True)
    city = models.CharField('Населенный пункт', max_length=101, blank=True)
    phone = models.CharField('Телефон', max_length=15, blank=True)
    status = models.ForeignKey(Status, verbose_name='Статус',
                               on_delete=models.PROTECT, default=1)
    position = models.ForeignKey(Position, verbose_name='Должность',
                                 on_delete=models.SET_NULL, null=True,
                                 blank=True)
    age = models.ForeignKey(Age, verbose_name='Возрастная категория',
                            on_delete=models.SET_NULL, null=True,
                            blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = (
            ("status_view", "Can status view"),)
        
    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                group = Group.objects.get(name=self.default_group_teacher)
                if group:
                    self.groups.add(group.id)
            except ObjectDoesNotExist:
                print('Group {} not exist'.format(self.default_group_teacher))

        super(CustomUser, self).save(*args, **kwargs)

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email
