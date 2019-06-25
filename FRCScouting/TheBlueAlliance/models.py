from django.db import models

class Team(models.Model):
    key = models.TextField()
    number = models.IntegerField()
    nickname = models.TextField()
    name = models.TextField()
    city = models.TextField()
    state_prov = models.TextField()
    country = models.TextField()
    address = models.TextField()
    postalcode = models.TextField()
    website = models.TextField()
    rookieyear = models.IntegerField()
    motto = models.TextField()
    logo = models.ImageField(upload_to='images/')
