from django import template

register = template.Library()


@register.inclusion_tag("locations/location_recursive.html")
def show_location(location, indent_level=0):
    """
    Recursively displays a location and its children with indentation.
    """
    return {"location": location, "indent_level": indent_level}
