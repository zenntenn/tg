from django import template

register = template.Library()


@register.filter(name="reverse")
def reverse(value):
    """Reverses the given value."""
    return value[::-1]
