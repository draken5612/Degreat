from django.contrib import admin
from .models import ContactInquiry, GeneratorRentalRequest, ScaffoldRentalRequest


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'inquiry_type', 'created_at', 'responded']
    list_filter = ['inquiry_type', 'responded', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Inquiry', {
            'fields': ('inquiry_type', 'message')
        }),
        ('Status', {
            'fields': ('responded', 'created_at')
        }),
    )


@admin.register(GeneratorRentalRequest)
class GeneratorRentalRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'generator_type', 'rental_start_date', 'rental_end_date', 'responded']
    list_filter = ['generator_type', 'responded', 'rental_start_date']
    search_fields = ['name', 'email', 'phone', 'location']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone', 'location')
        }),
        ('Rental Details', {
            'fields': ('generator_type', 'quantity', 'rental_start_date', 'rental_end_date', 'notes')
        }),
        ('Status', {
            'fields': ('responded', 'created_at')
        }),
    )


@admin.register(ScaffoldRentalRequest)
class ScaffoldRentalRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'scaffold_type', 'rental_start_date', 'rental_end_date', 'responded']
    list_filter = ['scaffold_type', 'responded', 'rental_start_date']
    search_fields = ['name', 'email', 'phone', 'location']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone', 'location')
        }),
        ('Rental Details', {
            'fields': ('scaffold_type', 'quantity', 'rental_start_date', 'rental_end_date', 'notes')
        }),
        ('Status', {
            'fields': ('responded', 'created_at')
        }),
    )
