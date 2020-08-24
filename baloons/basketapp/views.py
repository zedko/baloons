from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from basketapp.models import Basket
from mainapp.models import Product


def get_basket(user):
    basket_items = []
    if user.is_authenticated:
        basket_items = Basket.objects.filter(user=user)
    return basket_items


@login_required
def basket(request):
    title = 'Оформление заказа'
    content = {
        'title': title,
        'basket': get_basket(request.user)
    }
    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_item = get_object_or_404(Basket, pk=pk)
    basket_item.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# TODO: update basket counter with AJAX when quantity changed

@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('add_datetime')

        try:
            basket_cost = basket_items[0].total_cost
        except IndexError as e:
            print(e)
            basket_cost = 0

        content = {
            'basket': basket_items,

        }

        result = render_to_string('basketapp/include/inc_basket_product_item.html', content)

        return JsonResponse({'result': result, 'new_summary_cost': basket_cost})
