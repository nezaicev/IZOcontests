# Generated by Django 3.1.2 on 2021-03-31 07:54

import ckeditor.fields
import contests.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

import contests.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Возраст',
                'verbose_name_plural': 'Возраст',
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
                ('name', models.CharField(max_length=100, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материал',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mymoskvichi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер')),
                ('barcode', models.CharField(max_length=15, verbose_name='Штрих-код')),
                ('fio', models.CharField(max_length=300, verbose_name='Участник')),
                ('fio_teacher', models.CharField(max_length=300, verbose_name='Педагог')),
                ('school', models.CharField(max_length=150, verbose_name='Образовательная организация')),
                ('city', models.CharField(blank=True, max_length=101, verbose_name='Город')),
                ('year_contest', models.CharField(default='2020-2021 год', max_length=20, verbose_name='Год проведения')),
                ('date_reg', models.DateTimeField(auto_now=True)),
                ('nomination', models.CharField(max_length=50, verbose_name='Номинация')),
                ('nomination_extra', models.CharField(max_length=50, verbose_name='Доп.номинация')),
                ('author_name', models.CharField(max_length=50, verbose_name='Авторское название')),
                ('program', models.CharField(max_length=100, null=True, verbose_name='Программа(ы), в которой выполнена работа')),
                ('age', models.CharField(max_length=50, null=True, verbose_name='Возрастная категория')),
                ('link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка на файл (облако)')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.district', verbose_name='Округ')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.region', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Конкурс Мы Москвичи (участники)',
                'verbose_name_plural': 'Конкурс Мы Москвичи (участники)',
            },
        ),
        migrations.CreateModel(
            name='MymoskvichiSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(choices=[('nomination', 'Номинация'), ('age', 'Возраст'), ('theme', 'Тема')], max_length=20, verbose_name='Название поля')),
                ('data', models.CharField(max_length=255, verbose_name='Данные')),
            ],
            options={
                'verbose_name': 'Список (Мы Москвичи)',
                'verbose_name_plural': 'Списки (Мы Москвичи)',
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
            name='PageContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Название конкурса')),
                ('logo', models.ImageField(upload_to=contests.utils.PathAndRename('PageContests/'), verbose_name='Логотип')),
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
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='TeacherExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО')),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.mymoskvichi', verbose_name='Педагог')),
            ],
            options={
                'verbose_name': 'Педагог',
                'verbose_name_plural': 'Педагоги',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='Фамилия, имя')),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.mymoskvichi', verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='NRusheva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер')),
                ('barcode', models.CharField(max_length=15, verbose_name='Штрих-код')),
                ('fio', models.CharField(max_length=300, verbose_name='Участник')),
                ('fio_teacher', models.CharField(max_length=300, verbose_name='Педагог')),
                ('school', models.CharField(max_length=150, verbose_name='Образовательная организация')),
                ('city', models.CharField(blank=True, max_length=101, verbose_name='Город')),
                ('year_contest', models.CharField(default='2020-2021 год', max_length=20, verbose_name='Год проведения')),
                ('date_reg', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=contests.utils.PathAndRename('nrusheva/'), verbose_name='Изображение')),
                ('author_name', models.CharField(max_length=50, verbose_name='Авторское название')),
                ('format', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3')], max_length=2, verbose_name='Формат работы')),
                ('description', models.TextField(max_length=500, verbose_name='Аннотация')),
                ('age', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.age', verbose_name='Возраст')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.district', verbose_name='Округ')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.level', verbose_name='Класс')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.material', verbose_name='Материал')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.region', verbose_name='Регион')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contests.status', verbose_name='Статус')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.theme', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Конкурс им. Нади Рушевой (участник)',
                'verbose_name_plural': 'Конкурс им. Нади Рушевой (участники)',
            },
        ),
        migrations.AddField(
            model_name='mymoskvichi',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contests.status', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='mymoskvichi',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Artakiada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер')),
                ('barcode', models.CharField(max_length=15, verbose_name='Штрих-код')),
                ('fio', models.CharField(max_length=300, verbose_name='Участник')),
                ('fio_teacher', models.CharField(max_length=300, verbose_name='Педагог')),
                ('school', models.CharField(max_length=150, verbose_name='Образовательная организация')),
                ('city', models.CharField(blank=True, max_length=101, verbose_name='Город')),
                ('year_contest', models.CharField(default='2020-2021 год', max_length=20, verbose_name='Год проведения')),
                ('date_reg', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=contests.utils.PathAndRename('artakiada/'), verbose_name='Изображение')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='users.district', verbose_name='Округ')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.level', verbose_name='Класс')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.material', verbose_name='Материал')),
                ('nomination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.nomination', verbose_name='Номинация')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.region', verbose_name='Регион')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contests.status', verbose_name='Статус')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'АРТакиада (участник)',
                'verbose_name_plural': 'АРТакиада (участники)',
            },
        ),
    ]
