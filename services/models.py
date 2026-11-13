from django.db import models
from core.models import CroppableImageModel


class ServiceGalleryImage(CroppableImageModel):
    CATEGORY_CHOICES = [
        ('welding', 'Welding & Fabrication'),
        ('generators', 'Generator Rentals'),
        ('scaffolds', 'Scaffold Rentals'),
    ]

    title = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='service-gallery/')
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Service gallery image'
        verbose_name_plural = 'Service gallery images'

    def __str__(self):
        return self.title or self.get_category_display()


class Service(CroppableImageModel):
    """Welding and fabrication services"""
    SERVICE_TYPES = [
        ('argon', 'Argon Welding'),
        ('stainless', 'Stainless Steel Welding'),
        ('mild', 'Mild Steel Welding'),
        ('custom', 'Custom Metal Fabrication'),
        ('structural', 'Structural Steel Fabrication'),
    ]
    
    name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    description = models.TextField()
    features = models.TextField(help_text="Comma-separated list of features")
    applications = models.TextField(help_text="What it's used for")
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    gallery_images = models.ManyToManyField(ServiceGalleryImage, blank=True, related_name='welding_services')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.name


class Generator(CroppableImageModel):
    """Generator rental options"""
    GENERATOR_TYPES = [
        ('industrial', 'Industrial Generator'),
        ('petrol', 'Petrol Generator'),
        ('diesel', 'Diesel Generator'),
        ('gas', 'Gas-Powered Generator'),
    ]
    
    name = models.CharField(max_length=255)
    generator_type = models.CharField(max_length=50, choices=GENERATOR_TYPES)
    capacity_kva = models.IntegerField()
    power_type = models.CharField(max_length=50)
    description = models.TextField()
    features = models.TextField(help_text="Comma-separated list of features")
    applications = models.TextField(help_text="Best used for")
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weekly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monthly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='generators/', null=True, blank=True)
    gallery_images = models.ManyToManyField(ServiceGalleryImage, blank=True, related_name='generators')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['capacity_kva']
        verbose_name_plural = "Generators"
    
    def __str__(self):
        return f"{self.name} ({self.capacity_kva}kVA)"


class Scaffold(CroppableImageModel):
    """Scaffold rental options"""
    SCAFFOLD_TYPES = [
        ('construction', 'Construction Scaffolding'),
        ('access', 'Access Scaffolding'),
        ('modular', 'Modular Scaffolding'),
    ]
    
    name = models.CharField(max_length=255)
    scaffold_type = models.CharField(max_length=50, choices=SCAFFOLD_TYPES)
    description = models.TextField()
    features = models.TextField(help_text="Comma-separated list of features")
    applications = models.TextField(help_text="Best used for")
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weekly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monthly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='scaffolds/', null=True, blank=True)
    gallery_images = models.ManyToManyField(ServiceGalleryImage, blank=True, related_name='scaffolds')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Scaffolds"
    
    def __str__(self):
        return self.name
