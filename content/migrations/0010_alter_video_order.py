# Generated by Django 3.2 on 2023-08-10 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_alter_video_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='order',
            field=models.IntegerField(auto_created=True, blank=True, null=True, verbose_name='Порядковый номер'),
        ),
    ]