from django.shortcuts import redirect, render
from django.views import View

# Create your views here.
class ProfileView(View):
    """View for User Profiles"""

    def get(self, request):
        if request.user.is_authenticated:
            context = self.get_context(request.user)
            return render(request, "accounts/index.html", context,)
        return redirect("/accounts/login/")

    def get_context(self, user):
        return {}
