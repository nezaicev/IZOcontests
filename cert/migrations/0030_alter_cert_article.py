# Generated by Django 3.2 on 2023-01-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0029_cert_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cert',
            name='article',
            field=models.CharField(default='23', max_length=7, verbose_name='Артикул'),
        ),
    ]
