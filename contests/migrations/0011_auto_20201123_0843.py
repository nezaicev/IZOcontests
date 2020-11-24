# Generated by Django 3.1.2 on 2020-11-23 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0010_auto_20201122_2358'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Материал'),
        ),
        migrations.AddField(
            model_name='artakiada',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.level', verbose_name='Класс'),
        ),
    ]
