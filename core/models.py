from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import MaxValueValidator
from image_cropping import ImageRatioField


class ImageFocalPoint(models.Model):
    focal_x = models.PositiveSmallIntegerField(
        default=50,
        validators=[MaxValueValidator(100)],
        help_text='Horizontal subject position: 0 is left, 50 is center, 100 is right.',
    )
    focal_y = models.PositiveSmallIntegerField(
        default=65,
        validators=[MaxValueValidator(100)],
        help_text='Vertical subject position: 0 is top, 50 is center, 100 is bottom.',
    )

    class Meta:
        abstract = True


class CroppableImageModel(ImageFocalPoint):
    use_manual_crop = models.BooleanField(
        default=False,
        help_text='Only enable this when you want to crop the image instead of showing the full photo.',
    )
    cropping = ImageRatioField(
        'image',
        '960x540',
        size_warning=True,
        allow_fullsize=True,
        verbose_name='Manual crop',
        help_text='Drag and resize the selection to frame the work. The original photo is preserved.',
    )

    @property
    def has_manual_crop(self):
        return bool(self.use_manual_crop) and bool(self.cropping)

    class Meta:
        abstract = True


class ContactInquiry(models.Model):
    """Store contact form inquiries"""
    INQUIRY_TYPE_CHOICES = [
        ('welding', 'Welding Service Inquiry'),
        ('generator', 'Generator Rental Inquiry'),
        ('scaffold', 'Scaffold Rental Inquiry'),
        ('general', 'General Inquiry'),
    ]
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPE_CHOICES, default='general')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Contact Inquiries"
    
    def __str__(self):
        return f"{self.name} - {self.inquiry_type} - {self.created_at.strftime('%Y-%m-%d')}"


class GeneratorRentalRequest(models.Model):
    """Store generator rental requests"""
    GENERATOR_TYPE_CHOICES = [
        ('industrial_50', 'Industrial 50kVA Generator'),
        ('industrial_30', 'Industrial 30kVA Generator'),
        ('petrol_12', '12kVA Petrol Generator'),
        ('diesel_12', '12kVA Diesel Generator'),
        ('gas_15', 'Gas-Powered 15kVA Generator'),
    ]
    
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    generator_type = models.CharField(max_length=50, choices=GENERATOR_TYPE_CHOICES)
    quantity = models.IntegerField(default=1)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.generator_type} - {self.rental_start_date}"


class ScaffoldRentalRequest(models.Model):
    """Store scaffold rental requests"""
    SCAFFOLD_TYPE_CHOICES = [
        ('construction', 'Construction Scaffolding'),
        ('access', 'Access Scaffolding'),
        ('modular', 'Modular Scaffolding'),
    ]
    
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    scaffold_type = models.CharField(max_length=50, choices=SCAFFOLD_TYPE_CHOICES)
    quantity = models.IntegerField(default=1)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.scaffold_type} - {self.rental_start_date}"
