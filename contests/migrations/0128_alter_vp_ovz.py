# Generated by Django 3.2 on 2022-11-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0127_alter_vp_ovz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vp',
            name='ovz',
            field=models.BooleanField(default=False, null=True, verbose_name='Проект, выполнен детьми с ОВЗ'),
        ),
    ]