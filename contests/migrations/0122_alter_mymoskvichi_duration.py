# Generated by Django 3.2 on 2022-11-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0121_auto_20221109_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymoskvichi',
            name='duration',
            field=models.CharField(default='3:30', max_length=100, null=True, verbose_name='Длительность'),
        ),
    ]
