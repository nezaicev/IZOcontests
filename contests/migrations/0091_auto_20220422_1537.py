# Generated by Django 3.1.2 on 2022-04-22 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0090_auto_20220422_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['-rating'], 'verbose_name': 'Архив', 'verbose_name_plural': 'Архив'},
        ),
    ]
