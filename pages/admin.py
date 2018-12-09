from django.contrib import admin

from .models import PageMetadata, Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}

admin.site.register(PageMetadata)
admin.site.register(Page, PageAdmin)


