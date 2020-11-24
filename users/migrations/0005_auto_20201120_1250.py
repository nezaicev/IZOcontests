# Generated by Django 3.1.2 on 2020-11-20 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201120_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.district', verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='region',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.region', verbose_name='Регион'),
        ),
    ]
