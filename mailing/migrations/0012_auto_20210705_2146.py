# Generated by Django 3.1.2 on 2021-07-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0011_auto_20210526_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'Письмо', 'verbose_name_plural': 'Письма'},
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='region',
            field=models.CharField(choices=[('MSC', 'Москва и МО'), ('RG', 'Регион'), ('ALL', 'Всем'), ('MYSELF', 'Себе')], default='MSC', max_length=10, verbose_name='Регион'),
        ),
    ]