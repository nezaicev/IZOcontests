# Generated by Django 3.1.2 on 2021-08-18 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0032_auto_20210818_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecontest',
            options={'ordering': ('-id',), 'verbose_name': 'Страница мероприятия', 'verbose_name_plural': 'Страницы мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='showevent',
            options={'verbose_name': 'Публичное мероприятие', 'verbose_name_plural': 'Публичные мероприятия'},
        ),
    ]
