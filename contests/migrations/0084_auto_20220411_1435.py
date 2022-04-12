# Generated by Django 3.1.2 on 2022-04-11 14:35

import contests.models
import contests.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0083_auto_20220411_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extraimagearchive',
            options={'ordering': ['order_number'], 'verbose_name': 'Изображения архив', 'verbose_name_plural': 'Изображения архив'},
        ),
        migrations.AlterModelOptions(
            name='videoarchive',
            options={'ordering': ['order_number'], 'verbose_name': 'Видео архив', 'verbose_name_plural': 'Видео архив'},
        ),
        migrations.CreateModel(
            name='FileArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('file', models.FileField(max_length=200, upload_to=contests.models.PathAndRename('file/'), validators=[contests.validators.validate_file_extension], verbose_name='Файл')),
                ('files', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='contests.archive')),
            ],
            options={
                'verbose_name': 'Файлы архив',
                'verbose_name_plural': 'Файлы архив',
            },
        ),
    ]