from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from urllib.parse import quote
from .models import Generator, Scaffold, Service, ServiceGalleryImage
import json


def welding_services(request):
    """Display all welding services"""
    services = Service.objects.filter(active=True)
    
    context = {
        'services': services,
        'gallery_images': ServiceGalleryImage.objects.filter(category='welding'),
        'page_title': 'Welding & Fabrication Services - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Professional welding and metal fabrication services in Nigeria. Argon welding, stainless steel welding, mild steel welding, and custom fabrication.'
    }
    return render(request, 'services/welding_services.html', context)


def service_detail(request, service_id):
    """Detail view for individual service"""
    service = get_object_or_404(Service, id=service_id, active=True)
    
    context = {
        'service': service,
        'page_title': f'{service.name} - DE-GREAT WELD ENTERPRISES',
        'page_description': service.description[:160]
    }
    return render(request, 'services/service_detail.html', context)


def generator_rentals(request):
    """Display all generator rental options"""
    generators = Generator.objects.filter(active=True)
    
    context = {
        'generators': generators,
        'gallery_images': ServiceGalleryImage.objects.filter(category='generators'),
        'page_title': 'Generator Rentals - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Industrial and portable generator rental services in Nigeria. 12kVA, 30kVA, 50kVA and more available for rent by day, week, or month.'
    }
    return render(request, 'services/generator_rentals.html', context)


def generator_detail(request, generator_id):
    """Detail view for individual generator"""
    generator = get_object_or_404(Generator, id=generator_id, active=True)
    
    context = {
        'generator': generator,
        'page_title': f'{generator.name} Rental - DE-GREAT WELD ENTERPRISES',
        'page_description': generator.description[:160]
    }
    return render(request, 'services/generator_detail.html', context)


def scaffold_rentals(request):
    """Display all scaffold rental options"""
    scaffolds = Scaffold.objects.filter(active=True)
    
    context = {
        'scaffolds': scaffolds,
        'gallery_images': ServiceGalleryImage.objects.filter(category='scaffolds'),
        'page_title': 'Scaffold Rentals - DE-GREAT WELD ENTERPRISES',
        'page_description': 'Professional scaffolding rental services in Ikorodu, Lagos, and nationwide Nigeria. Construction, access, and modular scaffolding available.'
    }
    return render(request, 'services/scaffold_rentals.html', context)


def scaffold_detail(request, scaffold_id):
    """Detail view for individual scaffold type"""
    scaffold = get_object_or_404(Scaffold, id=scaffold_id, active=True)
    
    context = {
        'scaffold': scaffold,
        'page_title': f'{scaffold.name} Rental - DE-GREAT WELD ENTERPRISES',
        'page_description': scaffold.description[:160]
    }
    return render(request, 'services/scaffold_detail.html', context)


@require_http_methods(["POST"])
def request_rental(request):
    """Handle rental request via AJAX"""
    try:
        data = json.loads(request.body)
        
        rental_type = data.get('rental_type')  # 'generator' or 'scaffold'
        item_name = data.get('item_name')
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        quantity = data.get('quantity', 1)
        location = data.get('location')
        notes = data.get('notes', '')
        
        # Build WhatsApp message
        whatsapp_message = f"""Hi, I'm interested in renting {item_name}.

Details:
- Name: {name}
- Phone: {phone}
- Start Date: {start_date}
- End Date: {end_date}
- Quantity: {quantity}
- Location: {location}
- Notes: {notes}

Please confirm availability and pricing."""
        
        whatsapp_url = f"https://wa.me/234XXXXXXXXXX?text={quote(whatsapp_message)}"
        
        return JsonResponse({
            'status': 'success',
            'message': 'Rental request prepared. You will be redirected to WhatsApp.',
            'whatsapp_url': whatsapp_url
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
