from django.shortcuts import render
# from rest_framework import Response
from rest_framework.response import Response
from .models import Customer
from rest_framework.decorators import api_view
import json
# Create your views here.


@api_view(['POST'])
def submit_request(request):
    
    try:
        client_ip = request.META.get('REMOTE_ADDR')
        new_customer = Customer(email=request.data['email'], last_name=request.data['last_name'], national_id=request.data['national_id'], user_ip=client_ip, state="P")
        new_customer.save()
        return Response({"message": "DONE"}, status=200)
    except:
        return Response({"message": "ERROR"}, status=400)
    
    
@api_view(['POST'])
def get_status(request):
    try:
        client_ip = request.META.get('REMOTE_ADDR')
        national_id = request.data['national_id']
        customer = Customer.objects.get(national_id=national_id)
        if client_ip != customer.user_ip:
            return Response({"message": "Access Denied"})
        message = ''
        _s = customer.state
        if _s == "P":
            message = 'pending'
        elif _s == "r":
            message = 'rejected'
        else:
            message = 'approved'
        return Response({"details": message})
    except :
        return Response({"message": "ERROR"}, status=400)
        