from core.models import NewsItem

NewsItem.objects.get_or_create(
    title="Relaunch!",
    content="All the Exalted and CoD and Trinity stuff is gone, we're here for a leaner and more functional Tellurium Games, now in beta and ready to host a game. A few things left to do, so for now the site is password protected. Before going fully live, there will likely be another database reset, but poke around and see how things work. Anything you want to keep I'll do my best to recover it.",
    date="2024-09-21",
)
