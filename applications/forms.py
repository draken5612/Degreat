from django import forms
from .models import WelderApplication


class WelderApplicationForm(forms.ModelForm):
    class Meta:
        model = WelderApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'location',
            'experience_level', 'years_experience', 'specializations', 'certifications',
            'availability', 'can_travel', 'cv', 'portfolio_link', 'work_samples', 'cover_letter'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City/Location'}),
            'experience_level': forms.Select(attrs={'class': 'form-control'}),
            'years_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of Experience'}),
            'specializations': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'e.g., Argon welding, MIG welding, Stainless steel welding'}),
            'certifications': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'List your certifications'}),
            'availability': forms.Select(attrs={'class': 'form-control'}),
            'can_travel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cv': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf,.doc,.docx'}),
            'portfolio_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://your-portfolio.com'}),
            'work_samples': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*,video/*'}),
            'cover_letter': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tell us about yourself and why you\'d be a great fit for our team'}),
        }
