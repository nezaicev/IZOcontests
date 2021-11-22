# Generated by Django 3.1.2 on 2021-11-22 09:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0066_auto_20211120_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeART',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Возраст(Артакиада)',
                'verbose_name_plural': 'Возраст(Артакиада)',
            },
        ),
        migrations.AddField(
            model_name='artakiada',
            name='author_name',
            field=models.CharField(default=1, max_length=50, verbose_name='Авторское название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artakiada',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата Рождения'),
        ),
        migrations.AlterField(
            model_name='nrusheva',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 9, 41, 15, 160373, tzinfo=utc), verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='participantmymoskvichi',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 9, 41, 15, 169580, tzinfo=utc), verbose_name='Дата Рождения'),
        ),
        migrations.AlterField(
            model_name='teacherextramymoskvichi',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 9, 41, 15, 170230, tzinfo=utc), verbose_name='Дата Рождения'),
        ),
        migrations.AddField(
            model_name='artakiada',
            name='age',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.ageart', verbose_name='Возраст'),
        ),
    ]
