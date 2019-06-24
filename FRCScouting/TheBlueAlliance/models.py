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

    def summary(self):
        return self.body[:280]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title;
