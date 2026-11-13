from django.core.management.base import BaseCommand
from services.models import Service, Generator, Scaffold
from portfolio.models import Project
from datetime import date


class Command(BaseCommand):
    help = 'Populate database with initial dummy data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data initialization...'))

        # Create Services
        services_data = [
            {
                'name': 'Argon Welding',
                'service_type': 'argon',
                'description': 'Professional Argon welding services for precision work on aluminum, stainless steel, and other non-ferrous metals. Our certified welders use the latest equipment to ensure high-quality results.',
                'features': 'High precision, Clean welds, Excellent finish, Suitable for thin materials, Food-grade quality',
                'applications': 'Automotive parts, Aerospace components, Food industry equipment, Decorative metalwork',
            },
            {
                'name': 'Stainless Steel Welding',
                'service_type': 'stainless',
                'description': 'Expert stainless steel welding for corrosion-resistant applications. We specialize in all grades of stainless steel with proper heat treatment and finishing.',
                'features': 'Corrosion resistant, Food-safe materials, High strength, Professional finish, Hygienic quality',
                'applications': 'Kitchen equipment, Medical instruments, Chemical processing, Marine applications, Water treatment systems',
            },
            {
                'name': 'Mild Steel Welding',
                'service_type': 'mild',
                'description': 'Robust mild steel welding solutions for structural and general fabrication work. Fast, reliable, and cost-effective for heavy-duty applications.',
                'features': 'Cost-effective, High strength, Fast completion, Versatile applications, Durable results',
                'applications': 'Structural steel, Building frames, Machinery parts, Construction equipment, General fabrication',
            },
            {
                'name': 'Custom Metal Fabrication',
                'service_type': 'custom',
                'description': 'Bespoke metal fabrication services tailored to your specific requirements. From concept to completion, we deliver custom solutions.',
                'features': 'Customized design, Precision execution, Quality materials, Professional finishing, Expert consultation',
                'applications': 'Custom components, Architectural metalwork, Industrial equipment, Art installations, Specialized parts',
            },
            {
                'name': 'Structural Steel Fabrication',
                'service_type': 'structural',
                'description': 'Heavy-duty structural steel fabrication for major construction projects. We handle large-scale work with precision and expertise.',
                'features': 'High load capacity, Large-scale capability, Quality assurance, Professional installation, Engineering support',
                'applications': 'Building frameworks, Bridge components, Industrial structures, Heavy machinery mounts, Infrastructure projects',
            },
        ]

        for data in services_data:
            service, created = Service.objects.get_or_create(
                name=data['name'],
                defaults={
                    'service_type': data['service_type'],
                    'description': data['description'],
                    'features': data['features'],
                    'applications': data['applications'],
                    'active': True,
                }
            )
            if created:
                self.stdout.write(f'✓ Created service: {service.name}')

        # Create Generators
        generators_data = [
            {
                'name': 'Industrial 50kVA Diesel Generator',
                'generator_type': 'industrial',
                'capacity_kva': 50,
                'power_type': 'Diesel',
                'description': 'Heavy-duty industrial diesel generator perfect for large-scale welding operations, construction sites, and industrial use. Reliable power output with low fuel consumption.',
                'features': 'Fuel efficient, Durable construction, Quiet operation, Automatic controls, Weather resistant',
                'applications': 'Industrial welding, Large construction projects, Heavy machinery operation, Multiple tool usage, Event power supply',
                'daily_rate': 50000,
                'weekly_rate': 250000,
                'monthly_rate': 800000,
            },
            {
                'name': 'Industrial 30kVA Generator',
                'generator_type': 'industrial',
                'capacity_kva': 30,
                'power_type': 'Diesel',
                'description': 'Versatile mid-size industrial generator suitable for welding machines, cutting equipment, and general construction power needs.',
                'features': 'Reliable performance, Easy maintenance, Good fuel efficiency, Stable output, Portable design',
                'applications': 'Medium welding jobs, Construction sites, Cutting machine operation, Power backup, Events',
                'daily_rate': 35000,
                'weekly_rate': 175000,
                'monthly_rate': 600000,
            },
            {
                'name': '12kVA Petrol Generator',
                'generator_type': 'petrol',
                'capacity_kva': 12,
                'power_type': 'Petrol',
                'description': 'Compact and portable petrol generator ideal for small welding jobs, power tools, and portable welding machines. Easy to transport and operate.',
                'features': 'Lightweight, Portable, Quiet operation, Quick start, Low maintenance',
                'applications': 'Small welding projects, Portable tools, Emergency power, Site work, Outdoor events',
                'daily_rate': 15000,
                'weekly_rate': 75000,
                'monthly_rate': 250000,
            },
            {
                'name': 'Gas-Powered 15kVA Generator',
                'generator_type': 'gas',
                'capacity_kva': 15,
                'power_type': 'Gas-Powered',
                'description': 'Eco-friendly gas-powered generator offering clean, efficient power output. Suitable for welding operations and industrial applications.',
                'features': 'Clean energy, Efficient operation, Lower emissions, Stable output, Cost-effective',
                'applications': 'Welding operations, Industrial use, Site power, Green initiatives, Long-term operations',
                'daily_rate': 20000,
                'weekly_rate': 100000,
                'monthly_rate': 350000,
            },
        ]

        for data in generators_data:
            generator, created = Generator.objects.get_or_create(
                name=data['name'],
                defaults={
                    'generator_type': data['generator_type'],
                    'capacity_kva': data['capacity_kva'],
                    'power_type': data['power_type'],
                    'description': data['description'],
                    'features': data['features'],
                    'applications': data['applications'],
                    'daily_rate': data['daily_rate'],
                    'weekly_rate': data['weekly_rate'],
                    'monthly_rate': data['monthly_rate'],
                    'active': True,
                }
            )
            if created:
                self.stdout.write(f'✓ Created generator: {generator.name}')

        # Create Scaffolds
        scaffolds_data = [
            {
                'name': 'Construction Scaffolding',
                'scaffold_type': 'construction',
                'description': 'Professional construction scaffolding systems for building facades, maintenance work, and construction projects. Heavy-duty design built to withstand demanding conditions.',
                'features': 'Durable frames, Safety certified, Easy assembly, Quick installation, Professional support',
                'applications': 'Building construction, Facade work, Building maintenance, Construction sites, High-rise projects',
                'daily_rate': 25000,
                'weekly_rate': 125000,
                'monthly_rate': 400000,
            },
            {
                'name': 'Access Scaffolding',
                'scaffold_type': 'access',
                'description': 'Lightweight access scaffolding for maintenance, inspection, and repair work. Flexible and easy to set up at various locations.',
                'features': 'Lightweight, Portable, Flexible design, Safe access, Easy maintenance',
                'applications': 'Building maintenance, Inspection work, Repair projects, Painting work, Access platforms',
                'daily_rate': 15000,
                'weekly_rate': 75000,
                'monthly_rate': 250000,
            },
            {
                'name': 'Modular Scaffolding',
                'scaffold_type': 'modular',
                'description': 'Flexible modular scaffolding systems that can be customized for various applications. Mix and match components for your specific needs.',
                'features': 'Modular design, Customizable, Versatile components, Reusable elements, Easy reconfiguration',
                'applications': 'Custom projects, Event staging, Industrial maintenance, Temporary structures, Variable configurations',
                'daily_rate': 20000,
                'weekly_rate': 100000,
                'monthly_rate': 350000,
            },
        ]

        for data in scaffolds_data:
            scaffold, created = Scaffold.objects.get_or_create(
                name=data['name'],
                defaults={
                    'scaffold_type': data['scaffold_type'],
                    'description': data['description'],
                    'features': data['features'],
                    'applications': data['applications'],
                    'daily_rate': data['daily_rate'],
                    'weekly_rate': data['weekly_rate'],
                    'monthly_rate': data['monthly_rate'],
                    'active': True,
                }
            )
            if created:
                self.stdout.write(f'✓ Created scaffold: {scaffold.name}')

        # Create Projects
        projects_data = [
            {
                'title': 'Industrial Steel Frame Fabrication',
                'project_type': 'structural',
                'description': 'Large-scale structural steel fabrication project for a 5-storey industrial building. Involved cutting, welding, and assembly of complex structural components.',
                'client': 'ABC Construction Ltd',
                'location': 'Lagos Industrial District',
                'completion_date': date(2024, 6, 15),
                'featured': True,
            },
            {
                'title': 'Custom Stainless Steel Kitchen Equipment',
                'project_type': 'custom',
                'description': 'Fabrication of custom food-grade stainless steel equipment for a commercial kitchen. High precision welding and finishing to meet hygiene standards.',
                'client': 'Premium Catering Services',
                'location': 'Victoria Island, Lagos',
                'completion_date': date(2024, 5, 20),
                'featured': True,
            },
            {
                'title': 'Mild Steel Machinery Frame Assembly',
                'project_type': 'fabrication',
                'description': 'Assembly and welding of mild steel frames for heavy machinery. Included structural calculations and professional installation on-site.',
                'client': 'Industrial Manufacturing Co',
                'location': 'Ikorodu, Lagos',
                'completion_date': date(2024, 4, 10),
                'featured': True,
            },
        ]

        for data in projects_data:
            project, created = Project.objects.get_or_create(
                title=data['title'],
                defaults={
                    'project_type': data['project_type'],
                    'description': data['description'],
                    'client': data['client'],
                    'location': data['location'],
                    'completion_date': data['completion_date'],
                    'featured': data['featured'],
                }
            )
            if created:
                self.stdout.write(f'✓ Created project: {project.title}')

        self.stdout.write(self.style.SUCCESS('\n✅ Data initialization completed successfully!'))
        self.stdout.write(self.style.WARNING('\nNote: You can add images to these items through the Django admin at /admin'))
