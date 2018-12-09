from django.db import models

class Metadata(models.Model):
    label = models.CharField(
        max_length=200, 
        help_text='Enter the reference for this metadata (e.g. About page SEO)'
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(
        max_length=100, 
        blank=True
    )
    description = models.TextField(
        max_length=300, 
        blank=True
    )

    class Meta:
        verbose_name = 'metadata'
        verbose_name_plural = 'metadata'

    def __str__(self):
        return self.label
