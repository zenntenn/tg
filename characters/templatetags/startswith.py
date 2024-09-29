from django import template

register = template.Library()


@register.filter(name="startswith")
def startswith(s, q):
    return s.startswith(q)
