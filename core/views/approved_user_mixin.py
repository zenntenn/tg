from game.models import STRelationship


class SpecialUserMixin:
    def check_if_special_user(self, obj, user):
        if obj.owner is None:
            return True
        if user == obj.owner:
            return True
        if not user.is_authenticated:
            return False
        if STRelationship.objects.filter(user=user).count() > 0:
            return True
        return False
