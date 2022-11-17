# Generated by Django 3.2 on 2022-11-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0129_alter_vp_ovz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vp',
            name='ovz',
            field=models.CharField(choices=[('Нет', 'Нет'), ('Да', 'Да')], default='Нет', max_length=10, verbose_name='Проект, выполнен детьми с ОВЗ'),
        ),
    ]
