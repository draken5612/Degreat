from django.db import models
from django.core.validators import FileExtensionValidator


class WelderApplication(models.Model):
    """Welder job applications"""
    AVAILABILITY_CHOICES = [
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
        ('contract', 'Contract/Project-based'),
    ]
    
    EXPERIENCE_LEVELS = [
        ('beginner', 'Beginner (0-1 years)'),
        ('junior', 'Junior (1-3 years)'),
        ('intermediate', 'Intermediate (3-5 years)'),
        ('senior', 'Senior (5+ years)'),
    ]
    
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    
    # Professional Information
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVELS)
    years_experience = models.IntegerField()
    specializations = models.TextField(help_text="Comma-separated: e.g., Argon welding, Stainless steel welding, MIG welding")
    certifications = models.TextField(blank=True, help_text="List any welding certifications")
    
    # Availability
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    can_travel = models.BooleanField(default=True, help_text="Willing to travel for jobs")
    
    # Documents
    cv = models.FileField(upload_to='applications/cv/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])
    portfolio_link = models.URLField(blank=True, help_text="Link to portfolio or previous work samples")
    
    # Work Samples
    work_samples = models.FileField(upload_to='applications/samples/', null=True, blank=True, help_text="Photos or videos of previous work")
    
    # Additional
    cover_letter = models.TextField(blank=True)
    
    # Status
    status = models.CharField(max_length=20, default='new', choices=[
        ('new', 'New'),
        ('reviewed', 'Reviewed'),
        ('contacted', 'Contacted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    ])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Welder Application"
        verbose_name_plural = "Welder Applications"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
