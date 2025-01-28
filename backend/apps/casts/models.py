"""
Models for Casts App.
"""

from django.db import models

from apps.utils.models import BaseModel


class Director(BaseModel):
    """Model definition for Director."""

    name = models.CharField(max_length=255)

    class Meta:
        ordering: list[str] = ["pk"]
        verbose_name: str = "director"
        verbose_name_plural: str = "directors"

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return f"<Director(name='{self.name}')>"
