# Generated by Django 3.1.2 on 2021-05-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0005_auto_20210518_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filexls',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='phone',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='fio',
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='region',
            field=models.CharField(choices=[('MSC', 'Москва и МО'), ('RG', 'Регион')], default='MSC', max_length=10, verbose_name='Регион'),
        ),
    ]
