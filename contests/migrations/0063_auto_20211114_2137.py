# Generated by Django 3.1.2 on 2021-11-14 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0062_merge_20211110_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymoskvichi',
            name='theme',
        ),
        migrations.AlterField(
            model_name='nrusheva',
            name='info',
            field=models.ForeignKey(default=12, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.pagecontest'),
        ),
        migrations.AlterField(
            model_name='vp',
            name='info',
            field=models.ForeignKey(default=13, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.pagecontest'),
        ),
    ]