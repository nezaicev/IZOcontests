# Generated by Django 3.2 on 2023-09-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_publication_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер'),
        ),
    ]