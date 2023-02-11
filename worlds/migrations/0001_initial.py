# Generated by Django 4.1.5 on 2023-02-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Character",
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
                ("name", models.CharField(max_length=128)),
                ("nickname", models.CharField(max_length=128)),
                (
                    "character_type",
                    models.CharField(
                        choices=[
                            ("protagonist", "Protagonist"),
                            ("antagonist", "Antagonist"),
                            ("side_kick", "Side Kick"),
                            ("love_interest", "Love Interest"),
                            ("mentor", "Mentor"),
                            ("ally", "Ally"),
                            ("spirit", "Spirit"),
                            ("human", "Human"),
                            ("non_human", "Non-Human"),
                            ("animal", "Animal"),
                            ("monster", "Monster"),
                        ],
                        default="human",
                        max_length=32,
                    ),
                ),
                ("bio", models.TextField()),
                ("attributes", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=128)),
                ("desription", models.TextField()),
                ("attributes", models.TextField()),
                (
                    "landscape_type",
                    models.CharField(
                        choices=[
                            ("forest", "Forest"),
                            ("island", "Island"),
                            ("sea", "Sea"),
                            ("river", "River"),
                            ("ocean", "Ocean"),
                            ("mountain", "Mountain"),
                            ("desert", "Desert"),
                            ("plains", "Plains"),
                        ],
                        default="plains",
                        max_length=32,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Religions",
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
                ("name", models.CharField(max_length=128)),
                ("desription", models.TextField()),
                ("attributes", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="World",
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
                ("name", models.CharField(max_length=128, unique=True)),
                (
                    "world_type",
                    models.CharField(
                        choices=[
                            ("universe", "Universe"),
                            ("planet", "Planet"),
                            ("continent", "Continent"),
                            ("empire", "Empire"),
                            ("country", "Country"),
                            ("kingdom", "Kingdom"),
                            ("state", "State"),
                            ("region", "Region"),
                            ("city", "City"),
                            ("town", "Town"),
                        ],
                        default="kingdom",
                        max_length=32,
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
    ]
