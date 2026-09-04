from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class AccountView(APIView):
    def get(self, request):
        return Response({
            "message" : "Hello, World!"
        }, status=status.HTTP_200_OK)