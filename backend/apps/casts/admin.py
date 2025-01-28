"""
Admin for Casts App.
"""

from django.contrib import admin

from .models import Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    """Admin for Director model."""

    list_per_page = 25
    search_fields: list[str] = ["name"]
    list_display: list[str] = ["name", "is_available"]
    list_editable: list[str] = ["is_available"]
    readonly_fields: list[str] = ["pk", "created_at", "updated_at"]
    ordering: list[str] = ["pk"]
