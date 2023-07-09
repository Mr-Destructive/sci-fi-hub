# Generated by Django 4.1.7 on 2023-07-09 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("worlds", "0003_location_world_religions_world"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Religions",
            new_name="Religion",
        ),
        migrations.CreateModel(
            name="MagicSystem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField()),
                (
                    "world",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="worlds.world",
                    ),
                ),
            ],
        ),
    ]
