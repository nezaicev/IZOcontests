# Generated by Django 3.1.2 on 2022-10-11 10:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_auto_20221010_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participantevent',
            options={'permissions': [('export_participants', 'Выгрузить список участников')], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='event',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информация'),
        ),
    ]
