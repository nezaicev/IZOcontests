# Generated by Django 3.1.2 on 2020-11-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_auto_20201127_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artakiada',
            name='reg_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер'),
        ),
        migrations.AlterField(
            model_name='mymoskvichi',
            name='reg_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер'),
        ),
        migrations.AlterField(
            model_name='nrusheva',
            name='reg_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер'),
        ),
    ]
