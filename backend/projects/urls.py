from django.urls import path

from projects import views

urlpatterns = [
    path("", views.ProjectGraphQLView.as_view(), name='projects-gqlview'),
]
