# Generated by Django 3.2 on 2023-08-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20230810_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер'),
        ),
    ]
