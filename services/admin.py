from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import Generator, Scaffold, Service, ServiceGalleryImage


@admin.register(ServiceGalleryImage)
class ServiceGalleryImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'category', 'sort_order']
    list_filter = ['category']
    list_editable = ['sort_order']
    search_fields = ['title']
    ordering = ['category', 'sort_order']
    fields = ['title', 'category', 'image', 'use_manual_crop', 'cropping', 'sort_order']


@admin.register(Service)
class ServiceAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'service_type', 'active', 'created_at']
    list_filter = ['service_type', 'active', 'created_at']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Service Information', {
            'fields': ('name', 'service_type')
        }),
        ('Content', {
            'fields': ('description', 'features', 'applications')
        }),
        ('Images', {
            'fields': ('image', 'use_manual_crop', 'cropping', 'gallery_images')
        }),
        ('Status', {
            'fields': ('active',)
        }),
    )


@admin.register(Generator)
class GeneratorAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'capacity_kva', 'generator_type', 'power_type', 'daily_rate', 'active']
    list_filter = ['generator_type', 'active', 'capacity_kva']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Generator Information', {
            'fields': ('name', 'generator_type', 'power_type', 'capacity_kva')
        }),
        ('Content', {
            'fields': ('description', 'features', 'applications')
        }),
        ('Images', {
            'fields': ('image', 'use_manual_crop', 'cropping', 'gallery_images')
        }),
        ('Pricing', {
            'fields': ('daily_rate', 'weekly_rate', 'monthly_rate')
        }),
        ('Status', {
            'fields': ('active',)
        }),
    )


@admin.register(Scaffold)
class ScaffoldAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'scaffold_type', 'daily_rate', 'active']
    list_filter = ['scaffold_type', 'active']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Scaffold Information', {
            'fields': ('name', 'scaffold_type')
        }),
        ('Content', {
            'fields': ('description', 'features', 'applications')
        }),
        ('Images', {
            'fields': ('image', 'use_manual_crop', 'cropping', 'gallery_images')
        }),
        ('Pricing', {
            'fields': ('daily_rate', 'weekly_rate', 'monthly_rate')
        }),
        ('Status', {
            'fields': ('active',)
        }),
    )
