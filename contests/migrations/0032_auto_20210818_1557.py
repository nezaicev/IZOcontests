# Generated by Django 3.1.2 on 2021-08-18 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0031_auto_20210818_1411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='showevent',
            options={'ordering': ('-id',), 'verbose_name': 'Публичное мероприятие', 'verbose_name_plural': 'Публичные мероприятия'},
        ),
    ]
