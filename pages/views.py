from django.shortcuts import render, get_object_or_404
from .models import Page

PAGE_SUBTITLES = {
    "about": "Who we are and why we exist to support educators",
    "philosophy": "The principles that guide our work and partnerships",
}

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    subtitle = PAGE_SUBTITLES.get(slug, "Thoughtfully crafted content support for educators")
    return render(request, 'pages/page.html', {
        'page': page,
        'subtitle': subtitle
    })
