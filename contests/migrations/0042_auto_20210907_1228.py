# Generated by Django 3.1.2 on 2021-09-07 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0041_auto_20210906_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showevent',
            name='page_contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.pagecontest', verbose_name='Мероприятие'),
        ),
    ]