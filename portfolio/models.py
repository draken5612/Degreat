from django.db import models
from core.models import CroppableImageModel


class Project(CroppableImageModel):
    """Portfolio projects"""
    PROJECT_TYPES = [
        ('welding', 'Welding Project'),
        ('fabrication', 'Fabrication Project'),
        ('structural', 'Structural Steel'),
        ('custom', 'Custom Project'),
    ]
    
    title = models.CharField(max_length=255)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES)
    description = models.TextField()
    client = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    completion_date = models.DateField()
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='portfolio/')
    gallery_images = models.ManyToManyField('ProjectImage', blank=True, related_name='project')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-completion_date']
    
    def __str__(self):
        return self.title


class ProjectImage(CroppableImageModel):
    """Gallery images for projects"""
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='portfolio/gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['uploaded_at']
        verbose_name_plural = "Project Images"
    
    def __str__(self):
        return self.title or f"Image {self.id}"
