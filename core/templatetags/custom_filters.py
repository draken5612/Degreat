from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Split a string by the given delimiter.
    Usage: {{ string|split:"," }}
    """
    if value:
        return value.split(arg)
    return []