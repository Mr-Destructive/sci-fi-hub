import graphene
from graphene_django import DjangoObjectType

from worlds import models as world_models
from author import models as auth_models
from book import models as book_models

class WorldType(DjangoObjectType):
    class Meta:
        model = world_models.World


class CharacterType(DjangoObjectType):
    class Meta:
        model = world_models.Character


class AuthorType(DjangoObjectType):
    class Meta:
        model = auth_models.User


class BookType(DjangoObjectType):
    class Meta:
        model = book_models.Book


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    books_from_author = graphene.List(
        BookType, author_name=graphene.String(),
    )

    def resolve_authors(self, info):
        return auth_models.User.objects.all()

    def resolve_books(self, info):
        return book_models.Book.objects.all()

    def resolve_books_from_author(self, info, author_name):
        return book_models.Book.objects.filter(
            author__name = author_name,
        )


schema = graphene.Schema(query=Query)

