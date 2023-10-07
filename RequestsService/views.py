from django.shortcuts import render
# from rest_framework import Response
from rest_framework.response import Response
from .models import Customer
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer
# Create your views here.


@api_view(['GET'])
def ping(request):
    return Response({"PING": "PONG"})

@api_view(['POST'])
def submit_request(request):
    
    try:
        client_ip = request.META.get('REMOTE_ADDR')
        # print(Customer.objects.get(national_id = request.data['national_id']))
        customer_requests = Customer.objects.filter(national_id = request.data['national_id'])
        if len(customer_requests) != 0:
            for req in customer_requests:
                if req.state != "R":
                    return Response({"message": "Duplicate National_ID"})
            
            customer_requests[0].state = "P"
            customer_requests[0].save()
            return Response({"message": "Your Request Submited Again"})
        new_customer = Customer(email=request.data['email'], last_name=request.data['last_name'], national_id=request.data['national_id'], user_ip=client_ip, state="P")
        new_customer.save()
        return Response({"message": "Your Request Submited"}, status=200)
    except:
        return Response({"message": "ERROR"}, status=400)
    
    

    
    
@api_view(['POST'])
def get_status(request):
    try:
        client_ip = request.META.get('REMOTE_ADDR')
        national_id = request.data['national_id']
        customer = CustomerSerializer.objects.get(national_id=national_id)
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
        