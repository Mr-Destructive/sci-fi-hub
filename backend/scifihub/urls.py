from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import include, path
from graphene_django.views import GraphQLView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("", include('book.urls')),
    path("projects/", include('projects.urls')),
]
