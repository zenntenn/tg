from django import template

register = template.Library()


@register.filter(name="resonance")
def resonance(value):
    return value.resonance.through.objects.filter(mage=value)
