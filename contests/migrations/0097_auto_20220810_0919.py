# Generated by Django 3.1.2 on 2022-08-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0096_auto_20220810_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='contest_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Конкурс'),
        ),
    ]
