from django.http import HttpResponse
from django.template.loader import render_to_string

from categories.models import Category
from sites.models import Site


def show_main_page(request):
    sites = Site.objects.order_by('-id')[:5]

    result = render_to_string("index.html", {
        'sites': sites,
    })

    return HttpResponse(result)


def show_categories_page(request):
    categories = Category.objects.all()
    sites = Site.objects.all()[:10]

    result = render_to_string("categories.html", {
        'categories': categories,
        'sites': sites,
    })

    return HttpResponse(result)


def show_one_category(request, category_id):
    category = Category.objects.get(id=category_id)
    sites = category.sites.order_by('-id')()

    result = render_to_string("one_category.html", {
        "category": category,
        "sites": sites,
    })

    return HttpResponse(result)


def show_site_page(request, site_id):
    site = Site.objects.get(id=site_id)
    likes = site.likes.count()

    result = render_to_string("site.html", {
        "site": site,
        "likes": likes,
    })

    return HttpResponse(result)
