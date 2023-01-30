from django.db import models


class World(models.Model):
    class world_types(models.TextChoices):
        universe = 'universe', 'Universe'
        planet = 'planet', 'Planet'
        continent = 'continent', 'Continent'
        empire = 'empire', 'Empire'
        country = 'country', 'Country'
        kingdom = 'kingdom', 'Kingdom'
        state = 'state', 'State'
        region = 'region', 'Region'
        city = 'city', 'City'
        town = 'town', 'Town'

    name = models.CharField(max_length=128, unique=True)
    world_type = models.CharField(
            max_length=32, 
            choices=world_types.choices,
            default=world_types.kingdom
    )
