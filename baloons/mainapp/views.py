from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket


def get_basket(user):
    basket = []
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
    return basket


def index(request):
    products = Product.objects.all()
    context = {
        'title': 'main page',
        'products': products,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contacts.html', context)


def product_page(request, url_key=None):
    product = get_object_or_404(Product, id=url_key)
    title = product.short_desc
    suggestions = Product.objects.all()[:3]
    context = {
        'title': title,
        'product': product,
        'suggestions': suggestions,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/item.html', context)


