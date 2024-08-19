
class CaernDetailView(DetailView):
    model = Caern
    template_name = "wod/locations/werewolf/caern/detail.html"


class CaernCreateView(CreateView):
    model = Caern
    fields = "__all__"
    template_name = "wod/locations/werewolf/caern/form.html"


class CaernUpdateView(UpdateView):
    model = Caern
    fields = "__all__"
    template_name = "wod/locations/werewolf/caern/form.html"
