"""
Main Schemas.
"""

import graphene


from apps.movies.schema import MovieQuery, MovieMutation
from apps.categories.schema import GenreQuery, LanguageQuery, CountryQuery


class Query(
    MovieQuery,
    GenreQuery,
    LanguageQuery,
    CountryQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    MovieMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
