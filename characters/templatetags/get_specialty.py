from django import template

register = template.Library()


@register.filter(name="get_specialty")
def get_specialty(character, stat):
    return character.get_specialty(stat)
