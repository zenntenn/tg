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
        # Can be overridden to add additional conditions for key validity
        return key in self.view_mapping

    def get_default_redirect(self, request, *args, **kwargs):
        if isinstance(self.default_redirect, str):
            return redirect(self.default_redirect)
        elif callable(self.default_redirect):
            return self.default_redirect.as_view()(request, *args, **kwargs)
        raise ValueError("default_redirect must be a URL name or a view callable")
