# Generated by Django 3.1.2 on 2021-08-11 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0021_auto_20210810_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='contest',
            field=models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.PROTECT, to='contests.events', verbose_name='Конкурс/Мероприятие'),
        ),
    ]
