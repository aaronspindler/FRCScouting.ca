from django.db import models

class Team(models.Model):
    address = models.TextField(null=True)
    city = models.TextField(null=True)
    country = models.TextField(null=True)
    gmaps_place_id = models.TextField(null=True)
    gmaps_url = models.URLField(null=True)
    key = models.TextField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    location_name = models.TextField(null=True)
    motto = models.TextField(null=True)
    name = models.TextField(null=True)
    nickname = models.TextField(null=True)
    postal_code = models.TextField(null=True)
    rookie_year = models.IntegerField(null=True)
    state_prov = models.TextField(null=True)
    team_number = models.IntegerField(primary_key=True)
    website = models.URLField(null=True)

    #many to many
    #matches =
    #events =
