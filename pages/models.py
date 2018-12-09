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
    title = models.CharField(
        max_length=200,
        help_text='Set title to display in page and in navigation'
    )
    slug = models.SlugField(help_text='Set page url and database reference (auto-generated from title)')
    is_published = models.BooleanField(
        'Published', 
        default=False
    )
    is_homepage = models.BooleanField(
        'Home page', 
        default=False,
        help_text='Set page as home page without ambiguity'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title