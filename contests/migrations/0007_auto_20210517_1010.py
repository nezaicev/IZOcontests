# Generated by Django 3.1.2 on 2021-05-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0006_auto_20210514_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymoskvichiselect',
            name='data',
            field=models.CharField(max_length=500, verbose_name='Данные'),
        ),
    ]
