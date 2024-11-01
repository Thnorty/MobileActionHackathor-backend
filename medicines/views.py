from datetime import datetime
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
