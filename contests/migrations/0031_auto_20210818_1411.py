# Generated by Django 3.1.2 on 2021-08-18 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0030_auto_20210817_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecontest',
            options={'verbose_name': 'Страница мероприятия', 'verbose_name_plural': 'Страницы мероприятия'},
        ),
        migrations.CreateModel(
            name='ShowEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.CharField(max_length=20, unique=True, verbose_name='Регистрационный номер')),
                ('name', models.CharField(max_length=100, verbose_name='Название (конкурс/мероприятие)')),
                ('date_reg', models.DateTimeField(auto_now=True, verbose_name='Дата регистрации')),
                ('page_contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.pagecontest', verbose_name='Информация')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
