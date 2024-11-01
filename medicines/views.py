from datetime import datetime

from rest_framework.views import APIView
from django.http import JsonResponse


# Create your views here.
class HelloApiView(APIView):
    @staticmethod
    def get(request):
        datetime.now
        return JsonResponse({'message': 'Hello, World!'})
