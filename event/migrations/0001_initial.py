# Generated by Django 3.1.2 on 2022-09-07 13:02

import ckeditor.fields
import contests.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cert', '0024_merge_20220817_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350, verbose_name='Название мероприятия')),
                ('type', models.CharField(choices=[('Мероприятие', 'Мероприятие'), ('Анонс', 'Анонс')], default='Мероприятие', max_length=20, verbose_name='Тип')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=contests.utils.PathAndRename('PageContests/'), verbose_name='Изображение')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Контент')),
                ('send_letter', models.BooleanField(default=True)),
                ('letter', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Письмо')),
                ('certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cert.cert', verbose_name='Сертификат')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reg', models.DateTimeField(auto_now=True, verbose_name='Дата регистрации')),
                ('event', models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.PROTECT, to='event.event', verbose_name='Название')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
        ),
    ]