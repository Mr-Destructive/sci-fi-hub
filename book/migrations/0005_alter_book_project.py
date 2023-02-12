# Generated by Django 4.1.5 on 2023-02-12 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
        ("book", "0004_book_project_chapter_book_alter_chapter_section_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="project",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.project",
            ),
        ),
    ]
