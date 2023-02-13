from django.db import models
from author.models import User

from projects.models import Project


class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author",
    )
    genere = models.CharField(max_length=128)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.name + " : by " + self.author.username


class Section(models.Model):
    name = models.CharField(max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = [
            "book__id",
            "order",
        ]
        unique_together = (("book", "order"),)

    def __str__(self):
        return f"{self.book.name} -> {self.order} : {self.name}"


class Chapter(models.Model):
    name = models.CharField(max_length=128)
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    text_content = models.TextField()
    status = models.BooleanField(default=False, verbose_name="Publish")
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = [
            "section__order",
            "order",
        ]
        unique_together = (("section", "order"),)

    def __str__(self):
        book_name = self.section.book.name
        chapter_order = self.order
        return f"{book_name} : {chapter_order}"
