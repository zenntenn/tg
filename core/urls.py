from core import views
from django.urls import path

# Create your URLs here
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("book/<pk>/", views.BookDetailView.as_view(), name="book"),
    path(
        "language/create/",
        views.LanguageCreateView.as_view(),
        name="create_language",
    ),
    path("language/<pk>/", views.LanguageDetailView.as_view(), name="language"),
    path(
        "language/update/<pk>/",
        views.LanguageUpdateView.as_view(),
        name="update_language",
    ),
    path(
        "newsitem/create/",
        views.NewsItemCreateView.as_view(),
        name="create_newsitem",
    ),
    path("newsitem/<pk>/", views.NewsItemDetailView.as_view(), name="newsitem"),
    path(
        "newsitem/update/<pk>/",
        views.NewsItemUpdateView.as_view(),
        name="update_newsitem",
    ),
    path(
        "houserules/index/<gameline>/",
        views.HouseRulesIndexView.as_view(),
        name="houserules",
    ),
]
