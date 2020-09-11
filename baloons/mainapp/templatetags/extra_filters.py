from django import template
from baloons.settings import MEDIA_URL

register = template.Library()


@register.filter(name='range')
def range_filter(n: int):
    """Return an iterable list from a number given. n = range(number)"""
    try:
        n = range(n)
        n = [i + 1 for i in n]
    except Exception:
        n = n
    finally:
        return n


# TODO find where to fix /products_images/ part of the string when uploading via admin panel
@register.filter(name='product_image')
def product_image(string: str):
    default = 'default.jpg'
    if string:
        return f'{MEDIA_URL}products_images/{string}'
    else:
        return f'{MEDIA_URL}products_images/{default}'
