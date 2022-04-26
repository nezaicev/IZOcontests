# Generated by Django 3.1.2 on 2022-03-30 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0078_auto_20220328_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('video', models.URLField(verbose_name='Видео')),
                ('videos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='contests.vp', verbose_name='Видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='VideoArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('video', models.URLField(verbose_name='Видео')),
                ('order_number', models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер')),
                ('videos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='contests.archive')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
                'ordering': ['order_number'],
            },
        ),
    ]
