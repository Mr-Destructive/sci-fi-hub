from graphene_django.views import GraphQLView
from scifihub.schema import schema

class ProjectGraphQLView(GraphQLView):
    schema = schema
