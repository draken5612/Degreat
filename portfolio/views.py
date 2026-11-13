from django.shortcuts import render, get_object_or_404
from .models import Project


def portfolio(request):
    """Display all portfolio projects"""
    projects = Project.objects.all()
    project_type = request.GET.get('type')
    
    if project_type:
        projects = projects.filter(project_type=project_type)
    
    context = {
        'projects': projects,
        'project_type': project_type,
        'page_title': 'Portfolio - DE-GREAT WELD ENTERPRISES',
        'page_description': 'View our completed welding and fabrication projects. Industrial welding, metal fabrication, structural steel projects.'
    }
    return render(request, 'portfolio/portfolio.html', context)


def project_detail(request, project_id):
    """Detail view for individual project"""
    project = get_object_or_404(Project, id=project_id)
    related_projects = Project.objects.filter(project_type=project.project_type).exclude(id=project_id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
        'page_title': f'{project.title} - DE-GREAT WELD ENTERPRISES',
        'page_description': project.description[:160]
    }
    return render(request, 'portfolio/project_detail.html', context)
