from django import template

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
