"""
Schema for Movies App.
"""

import graphene
from graphene_django.types import DjangoObjectType
from django.db.models.manager import BaseManager

from .models import Movie


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields: str = "__all__"


class MovieQuery(graphene.ObjectType):
    movie = graphene.Field(MovieType, id=graphene.Int(required=True))

    def resolve_movie(self, info, id) -> Movie:
        return Movie.objects.get(id=id)

    all_movies = graphene.List(MovieType)

    def resolve_all_movies(self, info) -> BaseManager[Movie]:
        return Movie.objects.all()


class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)
        description = graphene.String()
        genre_id = graphene.Int()
        director_id = graphene.Int()
        language_id = graphene.Int()
        country_id = graphene.Int()
        trailer_url = graphene.String()
        cover = graphene.String()
        is_featured = graphene.Boolean()

    movie = graphene.Field(MovieType)

    def mutate(self, info, **kwargs) -> "CreateMovie":
        movie: Movie = Movie.objects.create(**kwargs)
        return CreateMovie(movie=movie)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        year = graphene.Int()
        description = graphene.String()
        genre_id = graphene.Int()
        director_id = graphene.Int()
        language_id = graphene.Int()
        country_id = graphene.Int()
        trailer_url = graphene.String()
        cover = graphene.String()
        is_featured = graphene.Boolean()

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, **kwargs) -> "UpdateMovie":
        movie = Movie.objects.get(id=id)
        for field, value in kwargs.items():
            if value is not None:
                setattr(movie, field, value)
        movie.save()
        return UpdateMovie(movie=movie)


class MovieMutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
