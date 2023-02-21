from django.shortcuts import render
from graphene_django.views import GraphQLView
from scifihub.schema import schema

class BookGraphQLView(GraphQLView):
    schema = schema
