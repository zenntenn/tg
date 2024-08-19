

from django.shortcuts import render
from characters.models.mage.mtahuman import MtAHuman


class MtAHumanView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        mtahuman = MtAHuman.objects.get(pk=kwargs["pk"])
        context = self.get_context(mtahuman)
        return render(request, "wod/characters/mage/mtahuman/detail.html", context)