# Generated by Django 3.2 on 2023-02-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221020_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fio',
            field=models.CharField(max_length=200, verbose_name='ФИО пользователя'),
        ),
    ]
