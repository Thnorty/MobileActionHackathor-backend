import random
import string
from django.db import models

from appointments.models import Appointment
from medicines.models import Medicine


# Create your models here.
class CareGiver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    reference_code = models.CharField(max_length=8, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.reference_code:
            self.reference_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        super().save(*args, **kwargs)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Senior(models.Model):
    caregiver = models.ForeignKey(CareGiver, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicines = models.ManyToManyField(Medicine, related_name='seniors', blank=True)
    appointments = models.ManyToManyField(Appointment, related_name='seniors', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
