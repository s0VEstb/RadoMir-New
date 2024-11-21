from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'genre', 'author_gmail', 'author')
    list_filter = ('genre', 'author_gmail')
    search_fields = ('title', 'description', 'author')


admin.site.register(models.Comment)
admin.site.register(models.Genre)

