from django.db import models


# Create your models here.
class Appointment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    place = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    attended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
