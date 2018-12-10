from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Page

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
    context = {
        'page': page,
        'metadata': page.metadata
    }
    return render(request, 'pages/about.html', context=context)
