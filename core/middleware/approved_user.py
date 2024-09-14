class UserListMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is an admin and set a flag
        if request.user.is_authenticated and request.user.is_staff:
            request.is_approved_user = True
        else:
            request.is_approved_user = False

        response = self.get_response(request)
        return response
