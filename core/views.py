from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    """This View controls the main landing page for the site"""

    def get(self, request):
        return render(request, "core/index.html", context={})
