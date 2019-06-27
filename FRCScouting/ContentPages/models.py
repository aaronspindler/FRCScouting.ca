from django.db import models

class GameManual(models.Model):
    year = models.CharField(max_length=4)
    name = models.CharField(max_length=140,null=True)
    file = models.FileField(upload_to='files/')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.year;
