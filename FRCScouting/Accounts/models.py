from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    country = CountryField(null=True)
    team_number = models.IntegerField(null=True)
    class Meta:
        db_table = 'auth_user'
