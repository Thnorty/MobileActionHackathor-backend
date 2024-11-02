from django.contrib import admin
from .models import CareGiver, Senior, Doctor

# Register your models here.
admin.site.register(CareGiver)
admin.site.register(Senior)
admin.site.register(Doctor)