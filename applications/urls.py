from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('', views.apply_now, name='apply'),
    path('success/', views.apply_success, name='apply_success'),
]
