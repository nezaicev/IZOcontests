# Generated by Django 3.1.2 on 2022-11-07 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0119_auto_20221026_1212'),
        ('cert', '0024_merge_20220817_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cert',
            name='contest',
            field=models.ForeignKey(blank=True, default=None, max_length=15, on_delete=django.db.models.deletion.PROTECT, to='contests.events', verbose_name='Конкурс'),
        ),
        migrations.AlterField(
            model_name='cert',
            name='status',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='contests.status', verbose_name='Статус участника'),
        ),
    ]