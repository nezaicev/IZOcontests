# Generated by Django 3.1.2 on 2021-07-13 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0016_auto_20210713_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='archive',
            name='teacher_extra',
        ),
    ]
