from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def get_basket(user):
    basket_items = []
    if user.is_authenticated:
        basket_items = Basket.objects.filter(user=user)
    return basket_items


def basket(request):
    title = 'Оформление заказа'
    content = {
        'title': title,
        'basket': get_basket(request.user)
    }
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basket.html', content)
