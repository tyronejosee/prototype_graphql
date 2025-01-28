"""
Schema for Casts App.
"""

import graphene
from django.db.models.manager import BaseManager

from .models import Director


class DirectorType(graphene.DjangoObjectType):
    class Meta:
        model = Director
        fields: str = "__all__"


class DirectorQuery(graphene.ObjectType):
    director = graphene.Field(DirectorType, id=graphene.Int(required=True))

    def resolve_director(self, info, id) -> Director:
        return Director.objects.get(id=id)

    all_movies = graphene.List(DirectorType)

    def resolve_all_movies(self, info) -> BaseManager[Director]:
        return Director.objects.all()
