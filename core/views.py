from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib import messages
from urllib.parse import quote
from .models import ContactInquiry, GeneratorRentalRequest, ScaffoldRentalRequest
from services.models import Service, Generator, Scaffold
from portfolio.models import Project
import json

def home(request):
    """Homepage with hero and service overview"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    services = Service.objects.filter(active=True)
    
    context = {
        'featured_projects': featured_projects,
        'services': services,
        'page_title': 'Home - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Professional metalworking and fabrication services in Nigeria. Welding, metal fabrication, and generator rentals.'
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page"""
    context = {
        'page_title': 'About Us - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Learn about DE-GREAT WELD ENTERPRISES, Nigeria\'s leading metalworking and fabrication company.'
    }
    return render(request, 'core/about.html', context)


@require_http_methods(["GET", "POST"])
def contact(request):
    """Contact page and form handler"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inquiry = ContactInquiry.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                phone=data.get('phone'),
                inquiry_type=data.get('inquiry_type', 'general'),
                message=data.get('message')
            )
            
            # Build WhatsApp message
            whatsapp_message = f"New inquiry from {data.get('name')}: {data.get('message')}"
            whatsapp_url = f"https://wa.me/{data.get('whatsapp_number')}?text={quote(whatsapp_message)}"
            
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you for your inquiry. We will contact you shortly.',
                'whatsapp_url': whatsapp_url
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    
    context = {
        'page_title': 'Contact Us - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Get in touch with DE-GREAT WELD ENTERPRISES for all your metalworking needs.'
    }
    return render(request, 'core/contact.html', context)


def whatsapp_redirect(request):
    """Redirect to WhatsApp with pre-filled message"""
    service_type = request.GET.get('service', 'general')
    phone = request.GET.get('phone', '')  # Will be set in settings
    
    messages_map = {
        'welding': 'Hi, I\'m interested in your welding services. Can you provide more information?',
        'argon': 'Hi, I\'m interested in Argon welding services. Can you tell me more about your services?',
        'stainless': 'Hi, I\'m interested in Stainless Steel welding. Do you provide this service?',
        'mild': 'Hi, I\'m interested in Mild Steel welding. Can you assist me?',
        'generator_industrial': 'Hi, I need to rent Industrial generators. What\'s your availability and pricing?',
        'generator_petrol': 'Hi, I need to rent a 12kVA petrol generator. What are your terms?',
        'generator_diesel': 'Hi, I need diesel generators for rent. Can you help?',
        'generator_gas': 'Hi, I\'m interested in renting gas-powered generators.',
        'scaffold': 'Hi, I need scaffolding rental services. Can you assist?',
        'hire': 'Hi, I\'m interested in applying as a welder for your team.',
        'general': 'Hi, I\'m interested in your services. Can you help me?'
    }
    
    message = messages_map.get(service_type, messages_map['general'])
    whatsapp_url = f"https://wa.me/234XXXXXXXXXX?text={quote(message)}"
    
    return redirect(whatsapp_url)


def faq(request):
    """FAQ page"""
    context = {
        'page_title': 'FAQ - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Frequently asked questions about our welding and generator rental services.'
    }
    return render(request, 'core/faq.html', context)


def privacy_policy(request):
    """Privacy policy page"""
    context = {
        'page_title': 'Privacy Policy - DE-GREAT WELD ENTERPRISES',
    }
    return render(request, 'core/privacy_policy.html', context)


def terms_conditions(request):
    """Terms and conditions page"""
    context = {
        'page_title': 'Terms & Conditions - DE-GREAT WELD ENTERPRISES',
    }
    return render(request, 'core/terms_conditions.html', context)
