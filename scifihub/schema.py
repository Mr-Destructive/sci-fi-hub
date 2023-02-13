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


class SectionType(DjangoObjectType):
    class Meta:
        model = book_models.Section


class ChapterType(DjangoObjectType):
    class Meta:
        model = book_models.Chapter


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    book_sections = graphene.List(
        SectionType,
        book_id=graphene.String(),
    )
    book_chapters = graphene.List(
        ChapterType,
        book_id=graphene.String(),
    )
    books_from_author = graphene.List(
        BookType,
        author_name=graphene.String(),
    )

    def resolve_authors(self, info):
        return auth_models.User.objects.all()

    def resolve_books(self, info):
        return book_models.Book.objects.all()

    def resolve_books_from_author(self, info, author_name):
        return book_models.Book.objects.filter(
            author__name=author_name,
        )

    def resolve_book_sections(self, info, book_id):
        return book_models.Section.objects.filter(
            book_id=book_id,
        )

    def resolve_book_chapters(self, info, book_id):
        return book_models.Chapter.objects.filter(
            section__book_id=book_id,
            status=True,
        )


schema = graphene.Schema(query=Query)
