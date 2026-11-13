from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import JsonResponse
from .models import WelderApplication
from .forms import WelderApplicationForm
import json


def apply_now(request):
    """Welder job application form"""
    if request.method == 'POST':
        form = WelderApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Your application has been received! We will review it and contact you shortly.')
            return redirect('apply:apply_success')
    else:
        form = WelderApplicationForm()
    
    context = {
        'form': form,
        'page_title': 'Apply as a Welder - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Join our team! Submit your application to work as a welder with DE-GREAT WELD ENTERPRISES.'
    }
    return render(request, 'applications/apply.html', context)


def apply_success(request):
    """Success page after application submission"""
    context = {
        'page_title': 'Application Received - DE-GREAT WELD ENTERPRISES',
    }
    return render(request, 'applications/apply_success.html', context)
