from django.contrib import admin

from .models import PartialsGroup, Partial, PageMetadata, Page

class PartialsGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ['name']}
    search_fields = ('name', 'slug')
    list_display_links = ('id', 'name')

class PartialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'page')
    search_fields = ('name', 'group', 'page')
    list_display_links = ('id', 'name')

class PartialInline(admin.StackedInline):
    model = Partial
    extra = 0

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
    inlines = [
      PartialInline
    ]

admin.site.register(PartialsGroup, PartialsGroupAdmin)
admin.site.register(Partial, PartialAdmin)
admin.site.register(PageMetadata, PageMetadataAdmin)
admin.site.register(Page, PageAdmin)
