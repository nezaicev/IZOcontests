# Generated by Django 3.1.2 on 2021-04-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0011_text_anchor'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='offset',
            field=models.IntegerField(default=3, verbose_name='Отступ (низ)'),
        ),
    ]
