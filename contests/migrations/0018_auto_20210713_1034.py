# Generated by Django 3.1.2 on 2021-07-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0017_auto_20210713_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archive',
            old_name='contest',
            new_name='contest_name',
        ),
    ]