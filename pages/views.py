from django.shortcuts import render
from django.http import HttpResponse

from .models import Page

def index(request):
    """View function for home page of site."""
    page = Page.objects.filter(is_published=True).get(is_homepage=True)
    context = {
        'page': page,
        'metadata': page.metadata
    }
    print(page)
    return render(request, 'pages/index.html', context=context)

def about(request):
    page = Page.objects.filter(is_published=True).get(slug='about')
    hero = page.partial_set.get(id=2)
    context = {
        'page': page,
        'metadata': page.metadata,
        'hero': hero
    }
    return render(request, 'pages/about.html', context=context)
