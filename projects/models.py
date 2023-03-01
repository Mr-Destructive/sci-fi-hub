from django.db import models

from author.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    desctription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project_type = models.CharField(max_length=64)
    status = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField()

    def __str__(self):
        return self.name
