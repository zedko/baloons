from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='media_product_image')
def media_product_image(string):
    """
    Добавляет путь к медиа папке из настроек,
    и показывает стандартное изображение,
    если у товара нет своего изображения
    """
    if not string:
        string = "default_image.jpg"
    return f'{settings.MEDIA_URL}{string}'
