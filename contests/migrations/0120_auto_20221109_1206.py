# Generated by Django 3.1.2 on 2022-11-09 09:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0119_auto_20221026_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherextramymoskvichi',
            name='birthday',
        ),
        migrations.AddField(
            model_name='mymoskvichi',
            name='address_school_gir',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес организации'),
        ),
        migrations.AddField(
            model_name='mymoskvichi',
            name='phone_gir',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Контактный телефон'),
        ),
        migrations.AddField(
            model_name='participantmymoskvichi',
            name='snils_gir',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='СНИЛС'),
        ),
        migrations.AlterField(
            model_name='participantmymoskvichi',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата Рождения'),
        ),
    ]
