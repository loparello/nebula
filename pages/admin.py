from django.contrib import admin

from .models import PageMetadata
from .models import Page

admin.site.register(PageMetadata)
admin.site.register(Page)
