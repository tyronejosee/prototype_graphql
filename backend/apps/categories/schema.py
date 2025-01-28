"""
Schema for Categories App.
"""

import graphene
from graphene_django.types import DjangoObjectType
from django.db.models.manager import BaseManager

from apps.categories.models import Genre, Language, Country


class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        fields: str = "__all__"


class LanguageType(DjangoObjectType):
    class Meta:
        model = Language
        fields: str = "__all__"


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields: str = "__all__"


class GenreQuery(graphene.ObjectType):
    genre = graphene.Field(GenreType, id=graphene.Int(required=True))

    def resolve_genre(self, info, id) -> Genre:
        return Genre.objects.get(id=id)

    all_genres = graphene.List(GenreType)

    def resolve_all_genres(self, info) -> BaseManager[Genre]:
        return Genre.objects.all()


class LanguageQuery(graphene.ObjectType):
    language = graphene.Field(LanguageType, id=graphene.Int(required=True))

    def resolve_language(self, info, id) -> Language:
        return Language.objects.get(id=id)

    all_languages = graphene.List(LanguageType)

    def resolve_all_languages(self, info) -> BaseManager[Language]:
        return Language.objects.all()


class CountryQuery(graphene.ObjectType):
    country = graphene.Field(CountryType, id=graphene.Int(required=True))

    def resolve_country(self, info, id) -> Country:
        return Country.objects.get(id=id)

    all_countries = graphene.List(CountryType)

    def resolve_all_countries(self, info) -> BaseManager[Country]:
        return Country.objects.all()
