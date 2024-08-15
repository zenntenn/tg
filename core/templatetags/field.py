from django import template

register = template.Library()


@register.filter(name="field")
def field(form, field_name):
    try:
        return form[field_name]
    except:
        return ""
