# Generated by Django 3.2 on 2023-06-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0146_auto_20230614_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creativetack',
            name='theme',
            field=models.CharField(max_length=200, verbose_name='Тема|Номинация'),
        ),
    ]
