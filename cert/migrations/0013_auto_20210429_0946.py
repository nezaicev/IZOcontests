# Generated by Django 3.1.2 on 2021-04-29 09:46

import cert.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0012_text_offset'),
    ]

    operations = [
        migrations.AddField(
            model_name='cert',
            name='article',
            field=models.CharField(default='21', max_length=7, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='cert',
            name='blank',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage, upload_to='certs/', validators=[cert.models.Cert.validate_image], verbose_name='Бланк сертификата'),
        ),
    ]
