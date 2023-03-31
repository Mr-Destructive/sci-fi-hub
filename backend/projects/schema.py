from author.models import User
import graphene
from graphene_django import DjangoObjectType
import projects.models as project_models


class ProjectType(DjangoObjectType):
    class Meta:
        model = project_models.Project

class Query(graphene.ObjectType):
    projects = graphene.List(
        ProjectType,
        author_id=graphene.ID(),
    )
    project = graphene.Field(
        ProjectType,
        project_id=graphene.ID(),
    )

    def resolve_projects(self, info):
        author_id = info.context.user.id
        return project_models.Project.objects.filter(
            author_id=author_id,
        )

    def resolve_project(self, info, project_id):
        author_id = info.context.user.id
        return project_models.Project.objects.get(
            author_id=author_id,
            id=project_id,
        )

class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False, default_value="")
        status = graphene.Boolean(required=False, default_value=True)

    project = graphene.Field(ProjectType)

    def mutate(self, info, name, description="", status=True):
        author = info.context.user
        if author:
            projects = project_models.Project.objects.filter(
                author_id=author.id, name=name
            )
            if projects:
                project = projects.first()
                project.description = description
                project.status = status
                project.save()
            else:
                project = project_models.Project.objects.create(
                    name=name,
                    description=description,
                    author_id=author.id,
                    status=status,
                )
            return CreateProject(project=project)


class UpdateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False)
        status = graphene.Boolean(required=False)

    project = graphene.Field(ProjectType)
    def mutate(self):
        pass


class DeleteProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False)
        status = graphene.Boolean(required=False)

    project = graphene.Field(ProjectType)
    def mutate(self):
        pass


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
