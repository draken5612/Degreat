from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('category', models.CharField(choices=[('welding', 'Welding & Fabrication'), ('generators', 'Generator Rentals'), ('scaffolds', 'Scaffold Rentals')], max_length=20)),
                ('image', models.ImageField(upload_to='service-gallery/')),
                ('sort_order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Service gallery image',
                'verbose_name_plural': 'Service gallery images',
                'ordering': ['sort_order', 'id'],
            },
        ),
    ]