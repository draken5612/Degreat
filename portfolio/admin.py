from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = Project.gallery_images.through
    extra = 1


@admin.register(ProjectImage)
class ProjectImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
    search_fields = ['title']
    fields = ['title', 'image', 'use_manual_crop', 'cropping']


@admin.register(Project)
class ProjectAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'project_type', 'client', 'completion_date', 'featured']
    list_filter = ['project_type', 'featured', 'completion_date']
    search_fields = ['title', 'description', 'client']
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'project_type', 'client', 'location')
        }),
        ('Content', {
            'fields': ('description', 'image', 'use_manual_crop', 'cropping', 'gallery_images')
        }),
        ('Dates', {
            'fields': ('completion_date',)
        }),
        ('Display', {
            'fields': ('featured',)
        }),
    )
