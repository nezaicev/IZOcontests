# Generated by Django 3.2 on 2023-09-29 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exposition', '0011_auto_20230928_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='exposition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='exposition.exposition', verbose_name='Выставка'),
        ),
    ]
