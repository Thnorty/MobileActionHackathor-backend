from django.urls import path
from . import views

urlpatterns = [
    path('emergency_phone/', views.EmergencyPhoneApiView.as_view(), name='index'),
    path('doctor_phone/', views.DoctorPhoneApiView.as_view(), name='index'),
    path('general_info/', views.GeneralInfoApiView.as_view(), name='index'),
]