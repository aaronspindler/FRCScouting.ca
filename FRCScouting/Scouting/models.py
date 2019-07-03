import uuid
from django.db import models

class stronghold_match(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.TextField(null=True)
    time_created = models.DateTimeField(null=True,auto_now=True)

    team_number = models.IntegerField(null=True)
    team_name = models.TextField(null=True)

    match_number = models.IntegerField(null=True)
    alliance_colour = models.IntegerField(null=True)

    highgoals = models.IntegerField(default=0)
    lowgoals = models.IntegerField(default=0)

    reach_defence = models.BooleanField(default=False)
    cross_Chevel_de_frise = models.BooleanField(default=False)
    cross_Drawbridge = models.BooleanField(default=False)
    cross_Lowbar = models.BooleanField(default=False)
    cross_Moat = models.BooleanField(default=False)
    cross_Portcullis = models.BooleanField(default=False)
    cross_Ramparts = models.BooleanField(default=False)
    cross_Rock_wall = models.BooleanField(default=False)
    cross_Rough_terrain = models.BooleanField(default=False)

    challenge = models.BooleanField(default=False)
    scale = models.BooleanField(default=False)

    blue_score = models.IntegerField(default=0)
    red_score = models.IntegerField(default=0)

    blue_foul = models.IntegerField(default=0)
    red_foul = models.IntegerField(default=0)

    driver_rating = models.IntegerField(default=0)
    robot_dead = models.BooleanField(default=False)

    comments = models.TextField(null=True)
