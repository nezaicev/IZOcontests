# Generated by Django 3.1.2 on 2020-11-22 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0008_artakiada_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['-name'], 'verbose_name': 'Материал', 'verbose_name_plural': 'Материал'},
        ),
    ]
