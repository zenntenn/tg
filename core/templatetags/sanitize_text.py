import bleach
from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter
def sanitize_html(value):
    allowed_tags = ["b", "i", "em", "strong", "p", "br", "strike", "ul", "li"]
    allowed_attributes = {}

    cleaned_text = bleach.clean(
        value, tags=allowed_tags, attributes=allowed_attributes, strip=True
    )
    return format_html(cleaned_text)
