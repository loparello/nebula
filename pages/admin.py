from django.contrib import admin

from .models import PageMetadata, Page

class PageMetadataAdmin(admin.ModelAdmin):
    list_display = ('label', 'page')
    search_fields = ('label', 'page')

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('id', 'title', 'slug', 'is_published', 'is_homepage')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'is_homepage')
    list_editable = ('is_published',)
    search_fields = ('title', 'slug')
    list_per_page = 25

admin.site.register(PageMetadata, PageMetadataAdmin)
admin.site.register(Page, PageAdmin)
