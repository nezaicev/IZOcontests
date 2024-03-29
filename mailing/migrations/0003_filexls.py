# Generated by Django 3.1.2 on 2021-05-18 21:50

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_auto_20210518_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileXls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage, upload_to='tmp/', verbose_name='Файл')),
                ('processed', models.BooleanField(default=False, verbose_name='Обработано')),
            ],
        ),
    ]
