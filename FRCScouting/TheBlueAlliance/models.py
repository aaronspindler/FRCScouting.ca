from django.db import models

class Team(models.Model):
    number = models.IntegerField(primary_key=True)
    key = models.TextField(null=True)
    nickname = models.TextField(null=True)
    name = models.TextField(null=True)
    city = models.TextField(null=True)
    state_prov = models.TextField(null=True)
    country = models.TextField(null=True)
    address = models.TextField(null=True)
    postalcode = models.TextField(null=True)
    website = models.TextField(null=True)
    rookieyear = models.IntegerField(null=True)
    motto = models.TextField(null=True)

    def location(self):
        return str("{}, {}, {}".format(city, state_prov, country))
