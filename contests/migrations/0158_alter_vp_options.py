# Generated by Django 3.2 on 2023-10-16 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0157_auto_20231016_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vp',
            options={'permissions': [('export_participants', 'Выгрузить список участников')], 'verbose_name': 'Заявка(у) на участие', 'verbose_name_plural': 'Конкурс Арт-проект'},
        ),
    ]
