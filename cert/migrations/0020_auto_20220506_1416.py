# Generated by Django 3.1.2 on 2022-05-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0019_cert_year_contest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cert',
            name='year_contest',
            field=models.CharField(max_length=20, null=True, verbose_name='Год'),
        ),
    ]