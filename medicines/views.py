from datetime import datetime, timedelta
from rest_framework.views import APIView
from django.http import JsonResponse
from api.models import Senior
from medicines.models import Medicine


# Create your views here.
class TodayMedicinesApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        senior = Senior.objects.get(id=senior_id)
        medicines = senior.medicines.filter(when_to_take__date=datetime.now().date())
        return JsonResponse(
            {
                'medicines': [
                    {
                        'id': medicine.id,
                        'name': medicine.name,
                        'description': medicine.description,
                        'time': medicine.when_to_take.strftime('%H:%M'),
                        'taken': medicine.taken,
                        'dosage': medicine.dosage
                    } for medicine in medicines
                ]
            }
        )


class ToggleMedicineApiView(APIView):
    @staticmethod
    def post(request):
        medicine_id = request.data.get('medicine_id')
        medicine = Medicine.objects.get(id=medicine_id)
        medicine.taken = not medicine.taken
        medicine.save()
        return JsonResponse({'message': 'Success'})


class AddMedicineApiView(APIView):
    @staticmethod
    def post(request):
        senior_id = request.data.get('senior_id')
        medicine_name = request.data.get('name')
        medicine_description = request.data.get('description')
        medicine_dosage = request.data.get('dosage')
        medicine_when_to_take = request.data.get('when_to_take')
        medicine_frequency_in_days = int(request.data.get('frequency_in_days'))
        medicine_is_empty_stomach = request.data.get('is_empty_stomach')

        senior = Senior.objects.get(id=senior_id)
        current_date = datetime.now().date()
        when_to_take_time = datetime.strptime(medicine_when_to_take, '%H:%M').time()
        medicines = []

        for i in range(0, 30, medicine_frequency_in_days):
            when_to_take_datetime = datetime.combine(current_date + timedelta(days=i), when_to_take_time)
            medicine = Medicine(
                name=medicine_name,
                description=medicine_description,
                is_empty_stomach=medicine_is_empty_stomach,
                dosage=medicine_dosage,
                when_to_take=when_to_take_datetime
            )
            medicine.save()
            medicines.append(medicine)

        senior.medicines.add(*medicines)
        return JsonResponse({'message': 'Success'})
