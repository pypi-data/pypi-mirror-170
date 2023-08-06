from django.db import models
from django.template.loader import render_to_string

from .requests import RequestService, get_request

DEFAULT_IMAGE_WIDTH = 1200
DEFAULT_IMAGE_HEIGHT = 800

class MetaForPage(models.Model):
	id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	page_url = models.CharField('Page Url', max_length=255, help_text='Enter the relative url eg. /contact-us. To use as the default enter "DEFAULT".')
	title = models.CharField('Title', max_length=255)
	description = models.CharField('Description', max_length=255)
	image = models.ImageField('Image', upload_to='page-meta/', 
							  height_field='image_height', width_field='image_width')
	image_height=models.PositiveIntegerField(blank=True)
	image_width=models.PositiveIntegerField(blank=True)
	keywords = models.CharField('Keywords', max_length=255, null=True, blank=True)

	class Meta:
		ordering = ('-id',)
		verbose_name = "Meta for Page"
		verbose_name_plural = "Meta for Pages"

	def __str__(self):
		return self.title

	@classmethod
	def get_default(cls):
		if cls.objects.filter(page_url__iexact='default').exists():
			return cls.objects.filter(page_url__iexact='default').first()
		return None
	
	@classmethod
	def get_from_current_url(cls):
		request_service = RequestService()
		qs = cls._default_manager.filter(
			models.Q(page_url=request_service.path) |
			models.Q(page_url=request_service.full_path)
		)
		return qs.first()

class Meta:
	'''
	Plain model for storing title description image keywords
	Also used for rendering
	'''

	class Image:
		def __init__(self, url, width=None, height=None) -> None:
			self.url, self.width, self.height = url, width, height
			self.width = self.width or DEFAULT_IMAGE_WIDTH
			self.height = self.height or DEFAULT_IMAGE_HEIGHT

	def __init__(self, *, title, description, image=None, image_url=None, image_width=None, image_height=None, keywords=None):
		self.title = title
		self.description = description
		self.keywords = keywords
		
		if image == None and image_url == None:
			raise ValueError('Both image or image_url cannot be empty.')

		request_service = RequestService()
		if image != None:
			self.image = image
			self.image_url = (request_service.get_full_url(path=image_url) 
							 if image_url else 
							 request_service.get_full_url(path=self.image.url))
			self.image_width = image_width or image.width or DEFAULT_IMAGE_WIDTH
			self.image_height = image_height or image.height or DEFAULT_IMAGE_HEIGHT
		else:
			self.image_url = request_service.get_full_url(path=image_url)
			self.image = Meta.Image(url=image_url, width=image_width, height=image_height)
			self.image_width = image_width or DEFAULT_IMAGE_WIDTH
			self.image_height = image_height or DEFAULT_IMAGE_HEIGHT

	def __str__(self):
		return self.render()

	def render(self):
		return render_to_string(template_name='pagemeta/meta.html', context={
			'meta': self,
			'request': get_request(),
		})
	
	@classmethod
	def get_default(cls):
		return cls.from_meta_for_page(MetaForPage.get_default())

	@classmethod
	def from_meta_for_page(cls, obj):
		if obj == None:
			return None
			
		return cls(
			title=obj.title,
			description=obj.description,
			image=obj.image,
			image_width=obj.image_width,
			image_height=obj.image_height,
			keywords=obj.keywords,
		)

	@staticmethod
	def none():
		return NoneMeta()
	
class NoneMeta:
	def __str__(self):
		return ''

	def __bool__(self):
		return False