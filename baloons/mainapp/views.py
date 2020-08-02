from django.shortcuts import render
import json
from .models import Product, ProductCategory


def index(request):
    with open('static/goods.json', 'r', encoding="utf8") as f:
        goods = json.load(f)
    products = Product.objects.all()
    context = {
        'title': 'main page',
        'goods': goods,
        'products': products
    }
    return render(request, 'mainapp/index.html', context)


def cart(request):
    context = {
        'title': 'cart',
    }
    return render(request, 'mainapp/cart.html', context)


def contacts(request):
    context = {
        'title': 'contacts',

    }
    return render(request, 'mainapp/contacts.html', context)


def product_page(request, url_key=None):
    print(url_key)
    product = Product.objects.filter(id=url_key)[0]
    title = product.short_desc
    suggestions = Product.objects.all()[:3]
    context = {
        'title': title,
        'product': product,
        'suggestions': suggestions
    }
    return render(request, 'mainapp/item.html', context)


