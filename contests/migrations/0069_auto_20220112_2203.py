# Generated by Django 3.1.2 on 2022-01-12 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0068_auto_20211122_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artakiada',
            name='info',
            field=models.ForeignKey(default=15, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.pagecontest'),
        ),
    ]
