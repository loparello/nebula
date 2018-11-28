from django.db import models

class Seo(models.Model):
    label = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=300, blank=True)
    def __str__(self):
        return self.label

class Page(models.Model):
    seo = models.OneToOneField(
        Seo, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField(blank=True)
    image_cover = models.ImageField('Cover', upload_to='images/%Y/%m/%d/')
    is_published = models.BooleanField('Published', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
