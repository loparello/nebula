from django.contrib import admin

from .models import PageMetadata, Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title', 'slug', 'is_published', 'is_homepage')
    list_filter = ('is_published', 'is_homepage')

admin.site.register(PageMetadata)
admin.site.register(Page, PageAdmin)


