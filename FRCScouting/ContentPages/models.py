from django.db import models

class GameManual(models.Model):
    year = models.CharField(max_length=4)
    file = models.FileField(upload_to='files/')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.year;
