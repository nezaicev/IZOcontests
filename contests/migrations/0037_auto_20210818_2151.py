# Generated by Django 3.1.2 on 2021-08-18 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0036_pagecontest_hide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontest',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
