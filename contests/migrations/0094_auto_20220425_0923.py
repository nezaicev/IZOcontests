# Generated by Django 3.1.2 on 2022-04-25 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0093_auto_20220425_0921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archive',
            options={'ordering': ['-rating', 'reg_number'], 'verbose_name': 'Архив', 'verbose_name_plural': 'Архив'},
        ),
    ]