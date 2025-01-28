"""
Admin for Categories App.
"""

from django.contrib import admin

from .models import Genre, Language, Country


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin for Genre model."""

    list_per_page = 25
    search_fields: list[str] = ["name"]
    list_display: list[str] = ["name", "is_available"]
    list_editable: list[str] = ["is_available"]
    readonly_fields: list[str] = ["pk", "created_at", "updated_at"]
    ordering: list[str] = ["pk"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """Admin for Language model."""

    list_per_page = 25
    search_fields: list[str] = ["name"]
    list_display: list[str] = ["name", "is_available"]
    list_editable: list[str] = ["is_available"]
    readonly_fields: list[str] = ["pk", "created_at", "updated_at"]
    ordering: list[str] = ["pk"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Admin for Country model."""

    list_per_page = 25
    search_fields: list[str] = ["name"]
    list_display: list[str] = ["name", "is_available"]
    list_editable: list[str] = ["is_available"]
    readonly_fields: list[str] = ["pk", "created_at", "updated_at"]
    ordering: list[str] = ["pk"]
