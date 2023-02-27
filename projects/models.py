from django.db import models

from author.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    desctription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
