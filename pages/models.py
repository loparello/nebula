from django.db import models

class Page(models.Model):
    seo = models.OneToOneField(
        'Seo', 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField(blank=True)
    image_cover = models.ImageField(upload_to='images/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


