"""
Models for Categories App.
"""

from django.db import models

from apps.utils.models import BaseModel


class Genre(BaseModel):
    """Model definition for Genre."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering: list[str] = ["pk"]
        verbose_name: str = "genre"
        verbose_name_plural: str = "genres"

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return f"<Genre(name='{self.name}')>"


class Language(BaseModel):
    """Model definition for Language."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering: list[str] = ["pk"]
        verbose_name: str = "language"
        verbose_name_plural: str = "languages"

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return f"<Language(name='{self.name}')>"


class Country(BaseModel):
    """Model definition for Country."""

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering: list[str] = ["pk"]
        verbose_name: str = "country"
        verbose_name_plural: str = "countries"

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return f"<Country(name='{self.name}')>"
