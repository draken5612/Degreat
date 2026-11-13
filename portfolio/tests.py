from datetime import date
from io import BytesIO
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from .models import Project, ProjectImage


def make_test_image(filename):
	image_buffer = BytesIO()
	Image.new('RGB', (1200, 675), color=(70, 90, 110)).save(image_buffer, format='JPEG')
	return SimpleUploadedFile(filename, image_buffer.getvalue(), content_type='image/jpeg')


class ProjectGalleryTests(TestCase):
	def setUp(self):
		media_directory = tempfile.TemporaryDirectory()
		self.addCleanup(media_directory.cleanup)
		media_settings = override_settings(MEDIA_ROOT=media_directory.name)
		media_settings.enable()
		self.addCleanup(media_settings.disable)

	def test_project_detail_shows_cover_and_gallery_photos_in_carousel(self):
		project = Project.objects.create(
			title='Workshop structure',
			project_type='fabrication',
			description='Custom fabricated workshop structure.',
			completion_date=date(2026, 1, 1),
			image=make_test_image('cover.jpg'),
			focal_x=32,
			focal_y=74,
		)
		project.gallery_images.add(ProjectImage.objects.create(
			title='Installation detail',
			image=make_test_image('installation.jpg'),
			focal_x=43,
			focal_y=81,
		))

		response = self.client.get(reverse('portfolio:project_detail', args=[project.id]))

		self.assertContains(response, 'data-photo-carousel')
		self.assertContains(response, 'cover.jpg')
		self.assertContains(response, 'installation.jpg')
		self.assertContains(response, 'Installation detail')
		self.assertContains(response, '--photo-focus-x: 32%; --photo-focus-y: 74%;')
		self.assertContains(response, '--photo-focus-x: 43%; --photo-focus-y: 81%;')
