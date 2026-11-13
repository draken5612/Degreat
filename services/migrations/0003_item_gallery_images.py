from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_servicegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='gallery_images',
            field=models.ManyToManyField(blank=True, related_name='welding_services', to='services.servicegalleryimage'),
        ),
        migrations.AddField(
            model_name='generator',
            name='gallery_images',
            field=models.ManyToManyField(blank=True, related_name='generators', to='services.servicegalleryimage'),
        ),
        migrations.AddField(
            model_name='scaffold',
            name='gallery_images',
            field=models.ManyToManyField(blank=True, related_name='scaffolds', to='services.servicegalleryimage'),
        ),
    ]