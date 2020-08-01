from django.shortcuts import render
import json


def index(request):
    with open('static/goods.json', 'r', encoding="utf8") as f:
        goods = json.load(f)

    context = {
        'title': 'main page',
        'goods': goods
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

