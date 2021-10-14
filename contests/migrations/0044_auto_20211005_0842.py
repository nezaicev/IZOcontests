# Generated by Django 3.1.2 on 2021-10-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0043_pagecontest_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontest',
            name='type',
            field=models.CharField(choices=[('1', 'Конкурс'), ('2', 'Мероприятие'), ('3', 'Анонс')], default=1, max_length=20, verbose_name='Тип'),
        ),
    ]