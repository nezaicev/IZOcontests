# Generated by Django 3.1.2 on 2022-04-12 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0086_auto_20220412_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['-rating'], 'verbose_name': 'Архив', 'verbose_name_plural': 'Архив'},
        ),
    ]
