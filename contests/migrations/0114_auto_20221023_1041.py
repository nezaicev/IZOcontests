# Generated by Django 3.1.2 on 2022-10-23 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0113_auto_20221021_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vp',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.directionvp', verbose_name='Форма организации'),
        ),
    ]
