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

    def ValidateTeamKey(self,team_key):
        def validate_key_name(self, team_key):
        key_name_regex = re.compile(r'^frc[1-9]\d*$')
        match = re.match(key_name_regex, team_key)
        return True if match else False
