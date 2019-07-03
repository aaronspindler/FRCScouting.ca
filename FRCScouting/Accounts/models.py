from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    country = models.TextField(null=True)
    team_number = models.IntegerField(null=True)
    class Meta:
        db_table = 'auth_user'
