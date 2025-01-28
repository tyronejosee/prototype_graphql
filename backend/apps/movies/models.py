"""
Models for Movies App.
"""

from datetime import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.casts.models import Director
from apps.categories.models import Genre, Language, Country
from apps.utils.models import BaseModel


class Movie(BaseModel):
    """Model definition for Movie."""

    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.now().year),
        ]
    )
    description = models.TextField()
    genre_id = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    director_id = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    director_id = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    language_id = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    country_id = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    trailer_url = models.URLField(blank=True, null=True)
    cover = models.ImageField(upload_to="movies/", blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.title)

    def __repr__(self) -> str:
        return f"<Movie(title='{self.title}', year='{self.year}')>"

    class Meta:
        ordering: list[str] = ["-year"]
        verbose_name: str = "movie"
        verbose_name_plural: str = "movies"
