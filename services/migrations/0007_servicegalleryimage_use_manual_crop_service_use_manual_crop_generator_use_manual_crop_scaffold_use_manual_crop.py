from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_generator_cropping_alter_scaffold_cropping_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicegalleryimage',
            name='use_manual_crop',
            field=models.BooleanField(default=False, help_text='Only enable this when you want to crop the image instead of showing the full photo.'),
        ),
        migrations.AddField(
            model_name='service',
            name='use_manual_crop',
            field=models.BooleanField(default=False, help_text='Only enable this when you want to crop the image instead of showing the full photo.'),
        ),
        migrations.AddField(
            model_name='generator',
            name='use_manual_crop',
            field=models.BooleanField(default=False, help_text='Only enable this when you want to crop the image instead of showing the full photo.'),
        ),
        migrations.AddField(
            model_name='scaffold',
            name='use_manual_crop',
            field=models.BooleanField(default=False, help_text='Only enable this when you want to crop the image instead of showing the full photo.'),
        ),
    ]
