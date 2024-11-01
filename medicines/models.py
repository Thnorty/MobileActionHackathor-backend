from django.db import models


# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_empty_stomach = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)
    dosage = models.CharField(max_length=100)
    when_to_take = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
