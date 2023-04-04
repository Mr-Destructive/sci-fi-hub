from author.models import User
import graphene
from graphene_django import DjangoObjectType
import worlds.models as world_models


class WorldType(DjangoObjectType):
    class Meta:
        model = world_models.World


class CharacterType(DjangoObjectType):
    class Meta:
        model = world_models.Character


class Query(graphene.ObjectType):
    worlds = graphene.List(
        WorldType,
        author_id=graphene.ID(),
    )
    world = graphene.Field(
        WorldType,
        project_id=graphene.ID(),
    )
    characters_for_author = graphene.List(
        CharacterType,
        author_id=graphene.ID(required=False),
    )
    characters_for_project = graphene.List(
        CharacterType,
        project_id=graphene.ID(),
    )
    characters_for_book = graphene.List(
        CharacterType,
        book_id=graphene.ID(),
    )
    character = graphene.Field(
        CharacterType,
        character_id=graphene.ID(),
    )

    def resolve_worlds(self, info):
        author_id = info.context.user.id
        return world_models.World.objects.filter(
            author_id=author_id,
        )

    def resolve_world(self, info, project_id):
        author_id = info.context.user.id
        return world_models.World.objects.get(
            author_id=author_id,
            id=project_id,
        )

    def resolve_characters_for_author(self, info, author_id):
        if not author_id:
            author_id = info.context.user.id
        return world_models.Character.objects.get(
            book__author_id=author_id,
        )

    def resolve_characters_for_project(self, info, project_id):
        author_id = info.context.user.id
        return world_models.Character.objects.get(
            project_id=project_id,
            project__author_id=author_id,
        )

    def resolve_characters_for_book(self, info, book_id):
        author_id = info.context.user.id
        return world_models.Character.objects.get(
            book_id=book_id,
            book__author_id=author_id,
        )


class CreateWorld(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False, default_value="")

    world = graphene.Field(WorldType)

    def mutate(self, info, name, description="", status=True):
        author = info.context.user
        if author:
            worlds = world_models.World.objects.filter(
                author_id=author.id, name=name
            )
            if worlds:
                world = worlds.first()
                world.description = description
                world.save()
            else:
                world = world_models.World.objects.create(
                    name=name,
                    description=description,
                    author_id=author.id,
                )
            return CreateWorld(world=world)


class Mutation(graphene.ObjectType):
    create_project = CreateWorld.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
