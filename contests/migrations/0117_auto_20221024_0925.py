# Generated by Django 3.1.2 on 2022-10-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0116_auto_20221023_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vp',
            name='level',
            field=models.ManyToManyField(related_name='levels', to='contests.LevelVP', verbose_name='Класс'),
        ),
    ]
