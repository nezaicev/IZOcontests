# Generated by Django 3.1.2 on 2020-11-27 10:42

import ckeditor.fields
import contests.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artakiada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=15, unique=True, verbose_name='Регистрационный номер')),
                ('fio', models.CharField(max_length=40, verbose_name='ФИО участника')),
                ('school', models.CharField(max_length=150, verbose_name='Образовательная организация')),
                ('city', models.CharField(blank=True, max_length=101, verbose_name='Город')),
                ('year_contest', models.CharField(default='2020-2021 год', max_length=20, verbose_name='Год проведения')),
                ('date_reg', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=contests.models.PathAndRename('artakiada/'), verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'АРТакиада (участник)',
                'verbose_name_plural': 'АРТакиада (участники)',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Класс',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материал',
            },
        ),
        migrations.CreateModel(
            name='Mymoskvichi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=15, unique=True, verbose_name='Регистрационный номер')),
                ('fio', models.CharField(max_length=40, verbose_name='ФИО участника')),
                ('school', models.CharField(max_length=150, verbose_name='Образовательная организация')),
                ('city', models.CharField(blank=True, max_length=101, verbose_name='Город')),
                ('year_contest', models.CharField(default='2020-2021 год', max_length=20, verbose_name='Год проведения')),
                ('date_reg', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Номинация')),
            ],
            options={
                'verbose_name': 'Номинация',
                'verbose_name_plural': 'Номинация',
            },
        ),
        migrations.CreateModel(
            name='NRusheva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=15, unique=True, verbose_name='Регистрационный номер')),
                ('fio', models.CharField(max_length=40, verbose_name='ФИО участника')),
                ('school', models.CharField(max_length=150, verbose_name='Образовательная организация')),
                ('city', models.CharField(blank=True, max_length=101, verbose_name='Город')),
                ('year_contest', models.CharField(default='2020-2021 год', max_length=20, verbose_name='Год проведения')),
                ('date_reg', models.DateTimeField(auto_now=True)),
                ('theme', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Название конкурса')),
                ('logo', models.ImageField(upload_to=contests.models.PathAndRename('PageContests/'), verbose_name='Логотип')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Страница конкурса',
                'verbose_name_plural': 'Страницы конкурсов',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=35, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статус',
            },
        ),
    ]
