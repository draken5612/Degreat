from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_cropping_alter_projectimage_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='use_manual_crop',
            field=models.BooleanField(default=False, help_text='Only enable this when you want to crop the image instead of showing the full photo.'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='use_manual_crop',
            field=models.BooleanField(default=False, help_text='Only enable this when you want to crop the image instead of showing the full photo.'),
        ),
    ]
