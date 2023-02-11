from django.db import models
from author.models import User


class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='book_author',
    )
    genere = models.CharField(max_length=128)
