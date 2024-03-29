# Generated by Django 3.1.2 on 2021-10-18 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0047_auto_20211018_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherExtraVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='ФИО')),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.vp', verbose_name='Педагог')),
            ],
            options={
                'verbose_name': 'Педагог',
                'verbose_name_plural': 'Педагоги',
            },
        ),
        migrations.CreateModel(
            name='ParticipantVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='Фамилия, имя')),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.vp', verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
    ]
