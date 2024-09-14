class SpecialUserMixin:
    def check_if_special_user(self, obj, user):
        if obj.owner is None:
            return True
        if user == obj.owner:
            return True
        if getattr(getattr(user, "profile", None), f"{obj.gameline}_st", None):
            return True
        return False
