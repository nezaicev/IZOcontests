# Generated by Django 3.1.2 on 2022-03-03 09:44

import contests.models
from django.db import migrations, models
import django.db.models.deletion

import contests.utils


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0073_auto_20220302_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraImageVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to=contests.utils.PathAndRename('all_contests/'), verbose_name='Изображение')),
                ('extra_images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vp', to='contests.vp', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='ExtraImageArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to=contests.utils.PathAndRename('all_contests/'), verbose_name='Изображение')),
                ('order_number', models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер')),
                ('extra_images', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archive', to='contests.archive', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
