# Generated by Django 3.1.2 on 2022-10-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_auto_20221011_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_date'], 'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AddField(
            model_name='event',
            name='reset_registration',
            field=models.BooleanField(default=False, verbose_name='Отмена регистрации'),
        ),
    ]
