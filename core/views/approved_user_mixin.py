class SpecialUserMixin:
    def check_if_special_user(self, obj, user):
        if obj.owner is None:
            return True
        if user == obj.owner:
            return True
        if getattr(user.profile, f"{obj.gameline}_st"):
            return True
        return False
