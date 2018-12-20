from django.db import models
from seo.models import Metadata

class PartialsGroup(models.Model):
    name = models.CharField(
      max_length=200,
      help_text='Set the reference group name'
    )
    slug = models.SlugField(
      help_text='Set a query-friendly label (auto-generated from name)'
    )

    class Meta:
        verbose_name = 'partials group'
        verbose_name_plural = 'partials groups'
    
    def __str__(self):
        return self.name

class Partial(models.Model):
    name = models.CharField(
      max_length=200,
      help_text='Set the reference partial name'
    )
    title = models.CharField(
      max_length=200,
      blank=True,
      help_text='The title to display in the partial'
    )
    subtitle = models.CharField(
      max_length=200,
      blank=True,
      help_text='The subtitle to display in the partial'
    )
    text = models.TextField(
      blank=True,
      help_text='The text body to display in the partial'
    )
    group = models.ForeignKey(
      PartialsGroup,
      on_delete=models.SET_NULL,
      blank=True,
      null=True,
      help_text='Arrange partials into groups'
    )

    def __str__(self):
        return self.name

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
    slug = models.SlugField(
        help_text='Set page url and database reference (auto-generated from title)'
    )
    is_published = models.BooleanField(
        'Is Published',
        default=False
    )
    is_homepage = models.BooleanField(
        'Is Homepage',
        default=False,
        help_text='Set page as home page without ambiguity'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    partials = models.ManyToManyField(
        Partial,
        blank=True,
        help_text='Add page partials'
    )

    def __str__(self):
        return self.title
