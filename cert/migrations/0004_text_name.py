# Generated by Django 3.1.2 on 2021-04-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0003_auto_20210423_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='name',
            field=models.CharField(default='Title', max_length=50, verbose_name='Название поля'),
        ),
    ]
