from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    # Welding services
    path('welding/', views.welding_services, name='welding_list'),
    path('welding/<int:service_id>/', views.service_detail, name='service_detail'),
    
    # Generator rentals
    path('generators/', views.generator_rentals, name='generator_list'),
    path('generators/<int:generator_id>/', views.generator_detail, name='generator_detail'),
    
    # Scaffold rentals
    path('scaffolds/', views.scaffold_rentals, name='scaffold_list'),
    path('scaffolds/<int:scaffold_id>/', views.scaffold_detail, name='scaffold_detail'),
    
    # Rental requests
    path('request-rental/', views.request_rental, name='request_rental'),
]
