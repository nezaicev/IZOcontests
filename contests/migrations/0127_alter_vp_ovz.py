# Generated by Django 3.2 on 2022-11-17 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0126_auto_20221111_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vp',
            name='ovz',
            field=models.BooleanField(default=False, verbose_name='Проект, выполнен детьми с ОВЗ'),
        ),
    ]
