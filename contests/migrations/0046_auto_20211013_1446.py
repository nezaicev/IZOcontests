# Generated by Django 3.1.2 on 2021-10-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0045_auto_20211012_1016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participant',
            new_name='ParticipantMymoskvichi',
        ),
        migrations.RenameModel(
            old_name='TeacherExtra',
            new_name='TeacherExtraMymoskvichi',
        ),
    ]