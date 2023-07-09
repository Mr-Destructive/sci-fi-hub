from django.contrib.auth.models import auth
from django.core.exceptions import PermissionDenied

import graphene
from graphene_django import DjangoObjectType

import projects.models as project_models
from author.models import User


class ProjectType(DjangoObjectType):
    class Meta:
        model = project_models.Project


class Query(graphene.ObjectType):
    projects = graphene.List(
        ProjectType,
        author_id=graphene.ID(default_value=None),
    )
    project = graphene.Field(
        ProjectType,
        project_id=graphene.ID(),
    )
    project_by_slug = graphene.Field(
        ProjectType,
        slug=graphene.String(),
    )

    def resolve_projects(self, info, author_id):
        user_id = info.context.user.id
        print(user_id, author_id)
        if author_id and author_id is not user_id:
            projects = project_models.Project.objects.filter(
                #visibility=project_models.Project.visiblity_types.public,
                author_id=author_id,
            )
        else:
            projects = project_models.Project.objects.filter(
                author_id=user_id,
            )
        return projects

    def resolve_project(self, info, project_id):
        user_id = info.context.user.id
        project = project_models.Project.objects.get(id=project_id)
        if project.author.id is not user_id:
            if project.visibility == project_models.Project.visiblity_types.public:
                return project
            else:
                return PermissionDenied
        else:
            return project

    def resolve_project_by_slug(self, info, slug):
        user_id = info.context.user.id
        project = project_models.Project.objects.get(slug=slug, author_id=user_id)
        if project.author.id is not user_id:
            if project.visibility == project_models.Project.visiblity_types.public:
                return project
            else:
                return PermissionDenied
        else:
            return project

class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False, default_value="")
        visibility = graphene.String(
            required=False, 
            default_value=project_models.Project.visiblity_types.private
        )
        status = graphene.String(required=False, default_value=project_models.Project.status_types.draft)
        project_type = graphene.String(required=False)

    project = graphene.Field(ProjectType)

    def mutate(self, info, name, description="", visibility=project_models.Project.visiblity_types.private, status=project_models.Project.status_types.draft, project_type=""):
        author = info.context.user
        if author:
            projects = project_models.Project.objects.filter(
                author_id=author.id, name=name, description=description,
                visibility=visibility, status=status, project_type=project_type
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
                    visibility=visibility,
                    status=status,
                    project_type=project_type,
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
