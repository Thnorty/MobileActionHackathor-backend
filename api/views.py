from datetime import datetime

from django.http import JsonResponse
from django.utils.timezone import make_aware
from rest_framework.views import APIView

from api.models import Senior


# Create your views here.
class EmergencyPhoneApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        senior = Senior.objects.get(id=senior_id)
        return JsonResponse({'phone': senior.caregiver.phone})


class DoctorPhoneApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        senior = Senior.objects.get(id=senior_id)
        return JsonResponse({'phone': senior.doctor.phone})


class GeneralInfoApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        senior = Senior.objects.get(id=senior_id)

        # Get the monthly info that has the taken medicines and missed, upcoming or went appointments
        monthly_info = {
            'medicines': [],
            'appointments': {
                'missed': [],
                'upcoming': [],
                'went': []
            }
        }

        # Get the medicines
        for medicine in senior.medicines.all():
            monthly_info['medicines'].append({
                'id': medicine.id,
                'name': medicine.name,
                'description': medicine.description,
                'taken': medicine.taken,
                'dosage': medicine.dosage,
                'when_to_take': medicine.when_to_take.strftime('%Y-%m-%d %H:%M'),
            })

        # Get the appointments
        current_time = make_aware(datetime.now())
        for appointment in senior.appointments.all():
            appointment_info = {
                'id': appointment.id,
                'title': appointment.title,
                'description': appointment.description,
                'place': appointment.place,
                'date_time': appointment.date_time.strftime('%Y-%m-%d %H:%M'),
                'attended': appointment.attended,
                'has_not_happened_yet': appointment.date_time > current_time
            }

            if appointment.date_time < current_time:
                monthly_info['appointments']['missed'].append(appointment_info)
            elif appointment.date_time > current_time:
                monthly_info['appointments']['upcoming'].append(appointment_info)
            else:
                monthly_info['appointments']['went'].append(appointment_info)

        return JsonResponse(monthly_info)