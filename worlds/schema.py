import graphene
from graphene_django import DjangoObjectType

from worlds import models

class WorldType(DjangoObjectType):
    class Meta:
        model = models.World


class CharacterType(DjangoObjectType):
    class Meta:
        model = models.Character

    
