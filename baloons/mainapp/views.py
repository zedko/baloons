from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def cart(request):
    return render(request, 'mainapp/cart.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

