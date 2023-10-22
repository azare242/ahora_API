from django.shortcuts import render
# from rest_framework import Response
from rest_framework.response import Response
from .models import Customer
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer
# Create your views here.
from PIL import Image
from .S3Service import S3
from .imagga import Imagga_Request
from .tasks import check_request, send_mail_submit, send_mail_resubmit
from .Messages import * 
from .mailgun import send_mail
from ipware import get_client_ip
@api_view(['GET'])
def ping(request):
    return Response({"PING": "PONG"})

@api_view(['POST'])
def submit_request(request):
    
    try:
        client_ip, _ = get_client_ip(request)
        customer_requests = Customer.objects.filter(national_id = request.data['national_id'])
        if len(customer_requests) != 0:
            for req in customer_requests:
                if req.state != "R":
                    return Response({"message": DUPLICATE}, status=400)
            
            customer_requests[0].state = "P"
            customer_requests[0].save()
            send_mail_resubmit(customer_requests[0])
            check_request.delay(customer_requests[0].email,
                                customer_requests[0].last_name,
                                customer_requests[0].img1.name.split('/')[-1],
                                customer_requests[0].img2.name.split('/')[-1])
            
            return Response({"message": RESUBMIT}, status=200)
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
        send_mail_submit.delay(new_customer.email,
                               new_customer.last_name
                               )
        check_request.delay(new_customer.email,
                            new_customer.last_name,
                            new_customer.img1.name.split('/')[-1],
                            new_customer.img2.name.split('/')[-1]
                            )
        return Response({"message": SUBMIT}, status=200)
    except Exception as exc:
        new_customer.delete()
        return Response({"message": str(exc)}, status=500)
    
    

    


@api_view(['POST'])
def get_status(request):
    try:
        client_ip, _ = get_client_ip(request)
            
        national_id = request.data['national_id']
        customer = Customer.objects.get(national_id=national_id)
        if client_ip != customer.user_ip:
            return Response({"message": ACCESS_DENIED}, status=403)
        message = ''
        _s = customer.state
        if _s == "P":
            message = PENDING
        elif _s == "r":
            message = REJECTED
        else:
            message = APPROVED
        return Response({"details": message}, status=200)
    except Exception as exc:
        return Response({"message": str(exc)}, status=500)
        
        
@api_view(['GET'])
def testing(request):
    try:
        send_mail_submit.delay('alireza', 'azare242@gmail.com')
        return Response({"message": "DONE"}, status=200)
    except Exception as exc:
        return Response({"message": str(exc)}, status=200)
                
@api_view(['GET'])
def echo_ip(request):
    _ip, _ = get_client_ip(request)
    return Response({"Message": _ip})
