from io import BytesIO
import tempfile

from django.contrib import admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from .models import Generator, Scaffold, Service, ServiceGalleryImage


def make_test_image(filename):
	image_buffer = BytesIO()
	Image.new('RGB', (1200, 675), color=(70, 90, 110)).save(image_buffer, format='JPEG')
	return SimpleUploadedFile(filename, image_buffer.getvalue(), content_type='image/jpeg')


class ServiceGalleryTests(TestCase):
	def setUp(self):
		media_directory = tempfile.TemporaryDirectory()
		self.addCleanup(media_directory.cleanup)
		media_settings = override_settings(MEDIA_ROOT=media_directory.name)
		media_settings.enable()
		self.addCleanup(media_settings.disable)

	def test_welding_page_only_shows_welding_gallery_images(self):
		ServiceGalleryImage.objects.create(
			title='Workshop welding',
			category='welding',
			image=make_test_image('welding.jpg'),
		)
		ServiceGalleryImage.objects.create(
			title='Generator delivery',
			category='generators',
			image=make_test_image('generator.jpg'),
		)

		response = self.client.get(reverse('services:welding_list'))

		self.assertContains(response, 'Workshop welding')
		self.assertContains(response, 'welding.jpg')
		self.assertNotContains(response, 'Generator delivery')
		self.assertNotContains(response, 'generator.jpg')

	def test_admin_image_form_uses_manual_crop_widget(self):
		form = admin.site._registry[ServiceGalleryImage].get_form(None)
		widget = form.base_fields['image'].widget

		self.assertEqual(type(widget).__name__, 'ImageCropWidget')
		self.assertIn('image_cropping/js/dist/image_cropping.min.js', str(widget.media))

	def test_each_service_and_rental_detail_shows_its_own_gallery(self):
		items = [
			(
				Service.objects.create(
					name='Argon Welding',
					service_type='argon',
					description='Argon welding service.',
					features='Clean welds',
					applications='Stainless steel work',
				),
				'services:service_detail',
				'services:welding_list',
				'welding',
				'argon-job.jpg',
			),
			(
				Generator.objects.create(
					name='Diesel Generator',
					generator_type='diesel',
					capacity_kva=30,
					power_type='Diesel',
					description='Diesel generator rental.',
					features='Reliable power',
					applications='Construction sites',
				),
				'services:generator_detail',
				'services:generator_list',
				'generators',
				'generator-job.jpg',
			),
			(
				Scaffold.objects.create(
					name='Construction Scaffold',
					scaffold_type='construction',
					description='Construction scaffolding rental.',
					features='Safe access',
					applications='Building work',
				),
				'services:scaffold_detail',
				'services:scaffold_list',
				'scaffolds',
				'scaffold-job.jpg',
			),
		]

		for item, detail_route, list_route, category, image_name in items:
			image = ServiceGalleryImage.objects.create(
				title=image_name,
				category=category,
				image=make_test_image(image_name),
				focal_x=40,
				focal_y=78,
			)
			item.gallery_images.add(image)

			detail_response = self.client.get(reverse(detail_route, args=[item.id]))
			list_response = self.client.get(reverse(list_route))

			self.assertContains(detail_response, image_name)
			self.assertContains(list_response, image_name)
			self.assertContains(list_response, image.image.url)
			self.assertContains(list_response, 'object-fit: contain;')
			self.assertNotContains(list_response, 'object-fit: cover; object-position: 40% 78%;')

	def test_manual_crop_is_used_when_selected(self):
		service = Service.objects.create(
			name='Custom Fabrication',
			service_type='custom',
			description='Custom fabrication service.',
			features='Precision welds',
			applications='Structural work',
		)
		image = ServiceGalleryImage.objects.create(
			title='custom-job.jpg',
			category='welding',
			image=make_test_image('custom-job.jpg'),
			use_manual_crop=True,
			cropping='15,10,85,72',
		)
		service.gallery_images.add(image)

		response = self.client.get(reverse('services:service_detail', args=[service.id]))

		self.assertContains(response, 'custom-job.jpg')
		self.assertContains(response, 'object-fit: cover;')
		self.assertContains(response, 'crop_detail.jpg')
