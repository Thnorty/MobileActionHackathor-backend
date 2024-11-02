from django.urls import path
from . import views

urlpatterns = [
    path('date_appointments/', views.DateAppointmentApiView.as_view(), name='date_appointments'),
    path('month_appointments/', views.MonthAppointmentApiView.as_view(), name='month_appointments'),
    path('add/', views.AddAppointmentApiView.as_view(), name='add_appointment'),
    path('toggle/', views.ToggleAppointmentApiView.as_view(), name='toggle_appointment'),
]