from core.models import Book, BookReference, Language, NewsItem
from django.contrib import admin

# Register your models here.
admin.site.register(NewsItem)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


admin.site.register(BookReference)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
