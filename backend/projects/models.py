from django.db import models

from author.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_type = models.CharField(max_length=64, null=True)
    status = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
