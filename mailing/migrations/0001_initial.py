# Generated by Django 3.1.2 on 2021-05-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('fio', models.CharField(blank=True, max_length=60, null=True, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('region', models.CharField(choices=[('Москва', 'Москва'), ('Регион', 'Регион')], max_length=10, verbose_name='Регион')),
            ],
        ),
    ]