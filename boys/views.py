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



@api_view(['GET'])
def payment(request):
    res = PayPingRequest().create_payment('123', 1000, 'alireza', '09019534878', "wolvahor@gmail.com", "test", PayPing_CALL_BACK);
    return Response(res)

@api_view(['POST'])
def verify_payment(request):
    return Response(request.POST)