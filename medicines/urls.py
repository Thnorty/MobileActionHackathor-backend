from django.urls import path
from . import views

urlpatterns = [
    path('today/', views.TodayMedicinesApiView.as_view(), name='index'),
    path('toggle/', views.ToggleMedicineApiView.as_view(), name='toggle'),
]