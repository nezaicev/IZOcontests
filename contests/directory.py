from django.db import models


class NominationVP(models.Model):
    name = models.CharField('Номинация', max_length=100)

    class Meta:
        verbose_name = 'Номинация(Выставочные проекты)'
        verbose_name_plural = 'Номинация(Выставочные проекты)'

    def __str__(self):
        return self.name


class DirectionVP(models.Model):
    name = models.CharField('Направление', max_length=100)

    class Meta:
        verbose_name = 'Направление(Выставочные проекты)'
        verbose_name_plural = 'Направление(Выставочные проекты)'

    def __str__(self):
        return self.name


class NominationNR(models.Model):
    name = models.CharField('Номинация', max_length=100)

    class Meta:
        verbose_name = 'Номинация(Н.Рушева)'
        verbose_name_plural = 'Номинация(Н.Рушева)'

    def __str__(self):
        return self.name


class AgeVP(models.Model):
    name = models.CharField('Возраст', max_length=10)

    class Meta:
        verbose_name = 'Возраст(Выставочные проекты)'
        verbose_name_plural = 'Возраст(Выставочные проекты)'

    def __str__(self):
        return self.name


class LevelVP(models.Model):
    name = models.CharField('Класс', max_length=10)

    class Meta:
        verbose_name = 'Класс(Выставочные проекты)'
        verbose_name_plural = 'Класс(Выставочные проекты)'

    def __str__(self):
        return self.name


class NominationART(models.Model):
    name = models.CharField('Номинация', max_length=100)

    class Meta:
        verbose_name = 'Номинация(Артакиада)'
        verbose_name_plural = 'Номинация(Артакиада)'

    def __str__(self):
        return self.name


class NominationMYMSK(models.Model):
    name = models.CharField('Номинация', max_length=100)

    class Meta:
        verbose_name = 'Номинация(Мы Москвичи)'
        verbose_name_plural = 'Номинация(Мы Москвичи)'

    def __str__(self):
        return self.name


class ThemeART(models.Model):
    name = models.CharField('Тема', max_length=200)

    class Meta:
        verbose_name = 'Тема(Артакиада)'
        verbose_name_plural = 'Темы(Артакиада)'

    def __str__(self):
        return self.name


class ThemeRUSH(models.Model):
    name = models.CharField('Тема', max_length=200)

    class Meta:
        verbose_name = 'Тема(Н.Рушева)'
        verbose_name_plural = 'Темы(Н.Рушева)'

    def __str__(self):
        return self.name


class ThemeMYMSK(models.Model):
    name = models.CharField('Тема', max_length=200)

    class Meta:
        verbose_name = 'Тема(Мы Москвичи)'
        verbose_name_plural = 'Тема(Мы Москвичи)'

    def __str__(self):
        return self.name


class AgeRUSH(models.Model):
    name = models.CharField('Возраст', max_length=10)

    class Meta:
        verbose_name = 'Возраст(Н.Рушева)'
        verbose_name_plural = 'Возраст(Н.Рушева)'

    def __str__(self):
        return self.name


class AgeART(models.Model):
    name = models.CharField('Возраст', max_length=10)

    class Meta:
        verbose_name = 'Возраст(Артакиада)'
        verbose_name_plural = 'Возраст(Артакиада)'

    def __str__(self):
        return self.name


class AgeMYMSK(models.Model):
    name = models.CharField('Возраст', max_length=60)

    class Meta:
        verbose_name = 'Возраст(Мы Москвичи)'
        verbose_name_plural = 'Возраст(Мы Москвичи)'

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
    name = models.CharField('Материал', max_length=100)

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
