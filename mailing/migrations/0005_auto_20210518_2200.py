# Generated by Django 3.1.2 on 2021-05-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_filexls_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filexls',
            name='name',
            field=models.CharField(default='Not name', max_length=100, verbose_name='Название'),
        ),
    ]
