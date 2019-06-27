from django.db import models

class ContactMessage(models.Model):
    sent_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
