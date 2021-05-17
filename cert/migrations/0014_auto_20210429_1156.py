# Generated by Django 3.1.2 on 2021-04-29 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cert', '0013_auto_20210429_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cert',
            name='level_text',
        ),
        migrations.RemoveField(
            model_name='cert',
            name='status_text',
        ),
        migrations.AddField(
            model_name='cert',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='status', to='cert.text', verbose_name='Должность/класс'),
            preserve_default=False,
        ),
    ]
