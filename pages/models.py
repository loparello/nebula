from django.db import models
from seo.models import Metadata

class PageMetadata(Metadata):
    class Meta:
        verbose_name = 'page metadata'
        verbose_name_plural = 'page metadata'

class Page(models.Model):
    metadata = models.OneToOneField(
        PageMetadata, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='Add metadata for page SEO'
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField(blank=True, help_text='Enter the main content of the page')
    image_cover = models.ImageField('Cover', upload_to='images/%Y/%m/%d/')
    is_published = models.BooleanField('Published', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
