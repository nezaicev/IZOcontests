# Generated by Django 3.1.2 on 2021-08-12 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0027_auto_20210811_1104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agemymsk',
            options={'verbose_name': 'Возраст(Мы Москвичи)', 'verbose_name_plural': 'Возраст(Мы Москвичи)'},
        ),
        migrations.AlterModelOptions(
            name='nominationart',
            options={'verbose_name': 'Номинация(Артакиада)', 'verbose_name_plural': 'Номинация(Артакиада)'},
        ),
        migrations.AlterModelOptions(
            name='nominationmymsk',
            options={'verbose_name': 'Номинация(Мы Москвичи)', 'verbose_name_plural': 'Номинация(Мы Москвичи)'},
        ),
    ]
