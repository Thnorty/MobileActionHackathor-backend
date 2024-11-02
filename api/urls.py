from django.urls import path
from . import views

urlpatterns = [
    path('emergency_phone/', views.EmergencyPhoneApiView.as_view(), name='index'),
    path('doctor_phone/', views.DoctorPhoneApiView.as_view(), name='index'),
    path('general_info/', views.GeneralInfoApiView.as_view(), name='index'),
    path('get_senior_location/', views.GetSeniorLocationApiView.as_view(), name='index'),
    path('update_senior_location/', views.UpdateSeniorLocationApiView.as_view(), name='index'),
    path('senior_fall_detection/', views.SeniorFallDetectionApiView.as_view(), name='index'),
    path('latest_fall_detection/', views.LatestFallDetectionApiView.as_view(), name='index'),
]