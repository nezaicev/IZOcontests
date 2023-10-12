# Generated by Django 3.2 on 2023-10-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0151_auto_20231006_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artakiada',
            options={'verbose_name': 'Заявку на участие', 'verbose_name_plural': 'Конкурс АРТакиада «Изображение и слово»'},
        ),
        migrations.AddField(
            model_name='artakiada',
            name='first_name',
            field=models.CharField(default=1, max_length=20, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artakiada',
            name='last_name',
            field=models.CharField(default=1, max_length=20, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artakiada',
            name='sur_name',
            field=models.CharField(default=1, max_length=20, verbose_name='Отчество'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artakiada',
            name='consent_personal_data',
            field=models.BooleanField(default=True, verbose_name='Согласие на обработку персональных данных участника(ов)'),
        ),
        migrations.AlterField(
            model_name='mymoskvichi',
            name='consent_personal_data',
            field=models.BooleanField(default=True, verbose_name='Согласие на обработку персональных данных участника(ов)'),
        ),
        migrations.AlterField(
            model_name='nrusheva',
            name='consent_personal_data',
            field=models.BooleanField(default=True, verbose_name='Согласие на обработку персональных данных участника(ов)'),
        ),
        migrations.AlterField(
            model_name='showevent',
            name='consent_personal_data',
            field=models.BooleanField(default=True, verbose_name='Согласие на обработку персональных данных участника(ов)'),
        ),
        migrations.AlterField(
            model_name='vp',
            name='consent_personal_data',
            field=models.BooleanField(default=True, verbose_name='Согласие на обработку персональных данных участника(ов)'),
        ),
    ]
