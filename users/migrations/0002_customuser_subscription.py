# Generated by Django 3.1.2 on 2021-05-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='subscription',
            field=models.BooleanField(default=True, verbose_name='Подписка'),
        ),
    ]