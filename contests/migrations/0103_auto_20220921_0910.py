# Generated by Django 3.1.2 on 2022-09-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0102_extraimagearchive_crop_orientation_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='showevent',
            options={'permissions': [('export_participants', 'Выгрузить список участников')], 'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterField(
            model_name='archive',
            name='crop_orientation_img',
            field=models.CharField(choices=[('top', 'Верх'), ('center', 'Центр'), ('bottom', 'Низ'), ('left', 'Лево'), ('right', 'Право')], default='center', max_length=50, verbose_name='Ориентация превью'),
        ),
        migrations.AlterField(
            model_name='extraimagearchive',
            name='crop_orientation_img',
            field=models.CharField(choices=[('top', 'Верх'), ('center', 'Центр'), ('bottom', 'Низ'), ('left', 'Лево'), ('right', 'Право')], default='center', max_length=50, verbose_name='Ориентация превью'),
        ),
    ]
