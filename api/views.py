from django.http import JsonResponse
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