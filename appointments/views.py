from datetime import datetime

from django.http import JsonResponse
from django.utils.timezone import make_aware
from rest_framework.views import APIView

from api.models import Senior
from appointments.models import Appointment


# Create your views here.
class DateAppointmentApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        date = request.data.get('date')

        senior = Senior.objects.get(id=senior_id)
        appointments = senior.appointments.filter(date_time__date=date).order_by('date_time')
        current_time = make_aware(datetime.now())

        return JsonResponse(
            {
                'appointments': [
                    {
                        'id': appointment.id,
                        'title': appointment.title,
                        'description': appointment.description,
                        'place': appointment.place,
                        'date_time': appointment.date_time.strftime('%Y-%m-%d %H:%M'),
                        'attended': appointment.attended,
                        'has_not_happened_yet': appointment.date_time > current_time,
                        'color': '#ffa500' if appointment.date_time > current_time else ('#3cc761' if appointment.attended else '#d60000')
                    } for appointment in appointments
                ]
            }
        )


class MonthAppointmentApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        year_month = request.data.get('year_month')  # year_month as 'YYYY-MM'

        senior = Senior.objects.get(id=senior_id)
        appointments = senior.appointments.filter(date_time__year=year_month[:4], date_time__month=year_month[5:]).order_by('date_time')
        current_time = make_aware(datetime.now())

        return JsonResponse(
            {
                'appointments': [
                    {
                        'id': appointment.id,
                        'title': appointment.title,
                        'description': appointment.description,
                        'place': appointment.place,
                        'date_time': appointment.date_time.strftime('%Y-%m-%d %H:%M'),
                        'attended': appointment.attended,
                        'has_not_happened_yet': appointment.date_time > current_time,
                        'color': '#ffa500' if appointment.date_time > current_time else ('#3cc761' if appointment.attended else '#d60000')
                    } for appointment in appointments
                ]
            }
        )


class AddAppointmentApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        title = request.data.get('title')
        description = request.data.get('description')
        place = request.data.get('place')
        date_time = request.data.get('date_time')

        senior = Senior.objects.get(id=senior_id)
        senior.appointments.create(title=title, description=description, place=place, date_time=date_time)

        return JsonResponse({'message': 'Appointment created successfully!'})


class ToggleAppointmentApiView(APIView):
    @staticmethod
    def post(request):
        appointment_id = request.data.get('appointment_id')

        appointment = Appointment.objects.get(id=appointment_id)
        appointment.attended = not appointment.attended
        appointment.save()

        return JsonResponse({'message': 'Appointment updated successfully!'})