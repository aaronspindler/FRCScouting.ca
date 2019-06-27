from django.db import models

class ContactMessage(models.Model):
    pub_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
