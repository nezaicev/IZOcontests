# Generated by Django 3.1.2 on 2022-01-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0069_auto_20220112_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='fio',
            field=models.CharField(max_length=700, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='artakiada',
            name='fio',
            field=models.CharField(max_length=700, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='mymoskvichi',
            name='fio',
            field=models.CharField(max_length=700, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='nrusheva',
            name='fio',
            field=models.CharField(max_length=700, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='showevent',
            name='fio',
            field=models.CharField(max_length=700, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='vp',
            name='fio',
            field=models.CharField(max_length=700, verbose_name='Участник'),
        ),
    ]
