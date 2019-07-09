from django.db import models
from Accounts.models import User

class Robot(models.Model):
    team_number = models.IntegerField()
    year = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='images/', blank=True, default=None)
    image2 = models.ImageField(upload_to='images/', blank=True)
    image3 = models.ImageField(upload_to='images/', blank=True)
    image4 = models.ImageField(upload_to='images/', blank=True)
    image5 = models.ImageField(upload_to='images/', blank=True)
    is_approved = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
