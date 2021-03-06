# Generated by Django 3.1.2 on 2020-11-28 23:31

import contests.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0006_auto_20201127_2003'),
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
        migrations.AlterModelOptions(
            name='nrusheva',
            options={'verbose_name': 'АРТакиада (участник)', 'verbose_name_plural': 'АРТакиада (участники)'},
        ),
        migrations.AddField(
            model_name='nrusheva',
            name='author_name',
            field=models.CharField(default=12345, max_length=50, verbose_name='Авторское название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nrusheva',
            name='description',
            field=models.TextField(default=123456, max_length=500, verbose_name='Аннотация'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nrusheva',
            name='format',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3')], default=1231231, max_length=2, verbose_name='Формат работы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nrusheva',
            name='image',
            field=models.ImageField(default=123123, upload_to=contests.models.PathAndRename('nrusheva/'), verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nrusheva',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.level', verbose_name='Класс'),
        ),
        migrations.AddField(
            model_name='nrusheva',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.material', verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='artakiada',
            name='fio',
            field=models.CharField(max_length=40, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='mymoskvichi',
            name='fio',
            field=models.CharField(max_length=40, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='nrusheva',
            name='fio',
            field=models.CharField(max_length=40, verbose_name='Участник'),
        ),
        migrations.AddField(
            model_name='nrusheva',
            name='age',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.age', verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='nrusheva',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.theme', verbose_name='Тема'),
        ),
    ]
