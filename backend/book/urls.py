from django.urls import path

from book import views

urlpatterns = [
    path("", views.BookGraphQLView.as_view(), name='book-gqlview'),
    path("chapters", views.ChapterGraphQLView.as_view(), name='chapters-gqlview'),
]
