import json

from django.forms.widgets import TextInput
from django.utils.html import escape
from django.utils.safestring import mark_safe


class AutocompleteTextInput(TextInput):
    def __init__(self, suggestions=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.suggestions = suggestions or []

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["suggestions"] = self.suggestions
        return context

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        suggestions_js = json.dumps(self.suggestions)
        autocomplete_js = """
            <script>
            $(function() {{
                var suggestions = {suggestions_js};
                $('input[name="{name}"]').autocomplete({{
                    source: suggestions,
                    minLength: 2
                }});
            }});
            </script>
        """.format(
            name=name, suggestions_js=suggestions_js
        )
        return mark_safe(html + autocomplete_js)
