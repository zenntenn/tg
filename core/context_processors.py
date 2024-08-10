from django.contrib.auth.models import User
from game.models import Chronicle


def all_chronicles(request):
    return {"chronicles": Chronicle.objects.all()}
