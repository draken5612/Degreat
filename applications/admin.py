from django.contrib import admin
from .models import WelderApplication


@admin.register(WelderApplication)
class WelderApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'experience_level', 'availability', 'status', 'created_at']
    list_filter = ['status', 'availability', 'experience_level', 'can_travel', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'location']
    readonly_fields = ['created_at', 'updated_at', 'full_name']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'first_name', 'last_name', 'email', 'phone', 'location')
        }),
        ('Professional Background', {
            'fields': ('experience_level', 'years_experience', 'specializations', 'certifications')
        }),
        ('Availability & Preferences', {
            'fields': ('availability', 'can_travel')
        }),
        ('Application Documents', {
            'fields': ('cv', 'portfolio_link', 'work_samples')
        }),
        ('Additional Information', {
            'fields': ('cover_letter',)
        }),
        ('Status', {
            'fields': ('status', 'created_at', 'updated_at')
        }),
    )
    
    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = "Applicant"
