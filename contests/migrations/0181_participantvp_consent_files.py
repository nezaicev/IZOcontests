import contests.utils
import contests.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0180_alter_mymoskvichi_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantvp',
            name='file_consent_personal_data_2',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to=contests.utils.PathAndRename('file/'), validators=[contests.validators.validate_consent_file_extension], verbose_name='Файл (Согласие 1, стр. 2)'),
        ),
        migrations.AlterField(
            model_name='participantvp',
            name='file_consent_personal_data',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to=contests.utils.PathAndRename('file/'), validators=[contests.validators.validate_consent_file_extension], verbose_name='Файл (Согласие 1, стр. 1)'),
        ),
        migrations.AlterField(
            model_name='participantvp',
            name='file_consent_non_commercial_use',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to=contests.utils.PathAndRename('file/'), validators=[contests.validators.validate_consent_file_extension], verbose_name='Файл (Согласие 2)'),
        ),
    ]
