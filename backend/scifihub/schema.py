import graphene
import graphql_jwt
from graphql_jwt.shortcuts import create_refresh_token, get_token
from graphql_jwt.decorators import login_required
from graphene_django import DjangoObjectType

from worlds import models as world_models
from author import models as auth_models
from book import models as book_models
from projects import models as project_models


class WorldType(DjangoObjectType):
    class Meta:
        model = world_models.World


class CharacterType(DjangoObjectType):
    class Meta:
        model = world_models.Character


class AuthorType(DjangoObjectType):
    class Meta:
        model = auth_models.User
        exclude = ('password',)


class BookType(DjangoObjectType):
    class Meta:
        model = book_models.Book


class SectionType(DjangoObjectType):
    class Meta:
        model = book_models.Section


class ChapterType(DjangoObjectType):
    class Meta:
        model = book_models.Chapter


class RevisionType(DjangoObjectType):
    class Meta:
        model = book_models.Revision


class ProjectType(DjangoObjectType):
    class Meta:
        model = project_models.Project


class DraftType(DjangoObjectType):
    class Meta:
        model = book_models.Draft

class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    book = graphene.Field(
        BookType,
        book_id=graphene.ID(),
    )
    chapter = graphene.Field(
        ChapterType,
        chapter_id=graphene.ID(),
    )
    book_sections = graphene.List(
        SectionType,
        book_id=graphene.String(),
    )
    book_chapters = graphene.List(
        ChapterType,
        book_id=graphene.ID(),
    )
    chapter_revisions = graphene.List(
        RevisionType,
        chapter_id=graphene.String(),
    )
    books_from_author = graphene.List(
        BookType,
        author_name=graphene.String(),
    )
    drafts_for_book = graphene.List(
        DraftType,
        book_id=graphene.String(),
    )
    projects_of_author = graphene.List(
        ProjectType,
        author_name=graphene.String(),
    )
    whoami = graphene.Field(AuthorType)

    @login_required
    def resolve_authors(self, info):
        return auth_models.User.objects.all()

    def resolve_books(self, info):
        author_id = info.context.user.id
        return book_models.Book.objects.filter(author_id=author_id)

    def resolve_books_from_author(self, info, author_name):
        return book_models.Book.objects.filter(
            author__username=author_name,
        )

    def resolve_book(self, info, book_id):
        return book_models.Book.objects.filter(
            id=book_id,
        ).first()

    def resolve_chapter(self, info, chapter_id):
        return book_models.Chapter.objects.filter(
            id=chapter_id,
        ).first()

    def resolve_book_sections(self, info, book_id):
        return book_models.Section.objects.filter(
            book_id=book_id,
        )

    def resolve_book_chapters(self, info, book_id):
        return book_models.Chapter.objects.filter(
            book_id=book_id,
        )

    def resolve_chapter_revisions(self, info, chapter_id):
        return book_models.Revision.objects.filter(
            revision__chapter_id=chapter_id,
        )
    def resolve_draft_for_book(self, info, book_id):
        return book_models.Draft.objects.filter(
            book_id=book_id,
        )

    def resolve_projects_of_author(self, info, author_name):
        return project_models.Project.objects.filter(
            author__name=author_name,
        )

    def resolve_whoami(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        return user

    viewer = graphene.Field(AuthorType)

    def resolve_viewer(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return user


class CreateAuthor(graphene.Mutation):
    author = graphene.Field(AuthorType)
    token = graphene.String()
    refresh_token = graphene.String()
    
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = auth_models.User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        token = get_token(user)
        refresh_token = create_refresh_token(user)
        return CreateAuthor(author=user, token=token, refresh_token=refresh_token)


class CreateBook(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, name):
        author = info.context.user
        book = book_models.Book.objects.create(name=name, author=author)
        return CreateBook(book=book)


class CreateChapter(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        book_id = graphene.ID(required=True)
        text_content = graphene.String(required=True)
        status = graphene.Boolean(required=False)
        order = graphene.Int(required=True)

    chapter = graphene.Field(ChapterType)

    def mutate(self, info, name, book_id, text_content, status, order):
        author = info.context.user
        book = book_models.Book.objects.filter(id=book_id).first()
        if book:
            if author.id == book.author.id:
                chapter = book_models.Chapter.objects.create(
                    name=name,
                    book_id=book_id,
                    text_content=text_content,
                    status=status,
                    order=order,
                )
                return CreateChapter(chapter=chapter)


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()    
    create_author = CreateAuthor.Field()
    create_book = CreateBook.Field()
    create_chapter = CreateChapter.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
