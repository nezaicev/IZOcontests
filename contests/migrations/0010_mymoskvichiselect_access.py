# Generated by Django 3.1.2 on 2021-06-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0009_auto_20210520_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymoskvichiselect',
            name='access',
            field=models.BooleanField(default=True, verbose_name='Доступ'),
        ),
    ]