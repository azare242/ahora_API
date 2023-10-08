from django.shortcuts import render
# from rest_framework import Response
from rest_framework.response import Response
from .models import Customer
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer
# Create your views here.
from PIL import Image
from .S3Service import S3

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
        new_customer = Customer(email=request.data['email'],
                                last_name=request.data['last_name'],
                                national_id=request.data['national_id'],
                                img1=request.data['img1'],
                                img2=request.data['img2'],
                                user_ip=client_ip, state="P")
        new_customer.save()
        s3 = S3()
        s3.insert_object(new_customer.img1.name)
        s3.insert_object(new_customer.img2.name)
        
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
        
        
        
@api_view(['POST'])
def test_images(request):
    try:
        customer = Customer.objects.get(email=request.data['email'])
        s3 = S3()
        a= s3.get_object(customer.img1.name.split('/')[-1])
        b= s3.get_object(customer.img2.name.split('/')[-1])
        print(a, b)
        return Response({"message": 'aha'})
    except Exception as exc:
        print(exc)
        return Response({"na": "da"})



@api_view(['GET'])
def run_s3(request):
    msg = ''
    try:
        s3 = S3()
        msg = 'ok'
    except Exception as ex:
        msg = 'error'
    return Response({"message" : msg})