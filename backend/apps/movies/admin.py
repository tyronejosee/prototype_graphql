"""
Admin for Movies App.
"""

from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin for Movie model."""

    list_per_page = 25
    search_fields: list[str] = ["title"]
    list_filter: list[str] = ["year", "genre_id"]
    list_display: list[str] = ["title", "year", "is_available"]
    list_editable: list[str] = ["is_available"]
    readonly_fields: list[str] = ["pk", "created_at", "updated_at"]
    ordering: list[str] = ["title"]
