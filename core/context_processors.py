from game.models import Chronicle


def all_chronicles(request):
    return {"chronicles": Chronicle.objects.all()}


def add_special_user_flag(request):
    return {
        "is_approved_user": getattr(request, "is_approved_user", False),
    }
