from django.shortcuts import render


def index(request):
    context = {
        'title': 'main page',

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

