from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from .payping import PayPingRequest, PayPing_CALL_BACK



class Ping(APIView):
    
    def get(self, request):
        return Response({"message": "PONG"}, status=status.HTTP_200_OK)



@api_view(['GET'])
def echo(request, msg):
    return Response({"you said": msg}, status=status.HTTP_200_OK)

