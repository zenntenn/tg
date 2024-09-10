from django.shortcuts import redirect
from django.views import View


class DictView(View):
    view_mapping = {}
    model_class = None
    key_property = None
    default_redirect = None

    def get_object(self, pk):
        return self.model_class.objects.get(pk=pk)

    def handle_request(self, request, *args, **kwargs):
        obj = self.get_object(kwargs["pk"])
        key = getattr(obj, self.key_property)

        if self.is_valid_key(obj, key):
            return self.view_mapping[key].as_view()(request, *args, **kwargs)

        return self.get_default_redirect(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.handle_request(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.handle_request(request, *args, **kwargs)

    def is_valid_key(self, obj, key):
        return key in self.view_mapping

    def get_default_redirect(self, request, *args, **kwargs):
        if isinstance(self.default_redirect, str):
            return redirect(self.default_redirect)
        elif callable(self.default_redirect):
            return self.default_redirect.as_view()(request, *args, **kwargs)
        raise ValueError("default_redirect must be a URL name or a view callable")


class MultipleFormsetsMixin:
    formsets = {}

    def get_formset_context(self, formset_class, formset_prefix):
        """Generate context and JavaScript code for a given formset."""
        formset = formset_class(prefix=formset_prefix)  # Initialize formset

        if len(formset.forms) == 0:
            formset = formset_class(
                initial=[{}], prefix=formset_prefix
            )  # Ensure at least one form exists

        empty_form = formset.empty_form  # Generate the "empty" form for cloning

        context = {
            "formset": formset,
            "formset_prefix": formset_prefix,
            "add_button_id": f"add_{formset_prefix}_form",
            "remove_button_class": f"remove_{formset_prefix}_form",
            "empty_form": empty_form,  # Pass empty form to context
        }

        js_code = f"""
        <script>
        document.getElementById('{context['add_button_id']}').addEventListener('click', function(e) {{
            e.preventDefault();  // Prevent form submission

            var totalForms = document.getElementById('id_{formset_prefix}-TOTAL_FORMS');
            var formCount = parseInt(totalForms.value);
            var emptyForm = document.getElementById('{formset_prefix}_empty_form').innerHTML;
            var newForm = emptyForm.replace(/__prefix__/g, formCount);  // Replace prefix
            document.getElementById('{formset_prefix}_container').insertAdjacentHTML('beforeend', newForm);
            totalForms.value = formCount + 1;
        }});
        </script>
        """

        return context, js_code

    def get_formsets(self):
        """Create and return all formsets defined in the view."""
        formsets_context = {}
        formsets_js = {}

        for prefix, formset_class in self.formsets.items():
            context, js_code = self.get_formset_context(formset_class, prefix)
            formsets_context[f"{prefix}_context"] = context
            formsets_js[f"{prefix}_js"] = js_code

        return formsets_context, formsets_js

    def get_context_data(self, **kwargs):
        """Add formsets and their context to the view context."""
        context = super().get_context_data(**kwargs)
        formsets_context, formsets_js = self.get_formsets()

        context.update(formsets_context)
        context.update(formsets_js)

        return context

    def form_valid(self, form):
        """Override to handle formsets saving logic."""
        formsets_context, _ = self.get_formsets()

        for prefix, formset_context in formsets_context.items():
            formset = formset_context["formset"]
            if not formset.is_valid():
                return self.form_invalid(form)  # Handle invalid formsets
            formset.save()  # Save valid formsets

        return super().form_valid(form)

    def get_form_data(self, formset_prefix):
        """
        Return a list of dictionaries containing the input data for all forms in the formset
        identified by the given prefix. The method works with POST data.
        """
        formset_class = self.formsets.get(formset_prefix)

        if not formset_class:
            return []  # Return an empty list if the formset prefix does not exist

        # Initialize the formset with POST data
        formset = formset_class(self.request.POST, prefix=formset_prefix)

        # Collect data from each form in the formset
        forms_data = []
        for i, form in enumerate(formset.forms):
            sample = {}
            for key in form.fields.keys():
                if f"{formset_prefix}-{i}-{key}" in form.data:
                    sample[key] = form.data[f"{formset_prefix}-{i}-{key}"]
            if sample:
                forms_data.append(sample)
        return forms_data
