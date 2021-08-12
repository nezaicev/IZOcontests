# Generated by Django 3.1.2 on 2021-04-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0006_auto_20210423_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='align',
            field=models.CharField(choices=[('center', 'center'), ('left', 'left'), ('right', 'right')], default='center', max_length=10, verbose_name='Выравнивание текста'),
        ),
        migrations.AddField(
            model_name='text',
            name='width',
            field=models.IntegerField(default=50, verbose_name='Длинна текста'),
        ),
        migrations.AlterField(
            model_name='text',
            name='color',
            field=models.CharField(default='#000000', max_length=7, verbose_name='Цвет текста'),
        ),
    ]