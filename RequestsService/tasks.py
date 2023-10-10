from celery import shared_task
from RequestsService.models import Customer
from RequestsService.S3Service import S3
from RequestsService.imagga import Imagga_Request
from RequestsService.Messages import *
from RequestsService.mailgun import send_mail


@shared_task
def send_mail_submit(customer):
    send_mail(
        EMAIL_SUBJECT_RESUBMIT,
        EMAIL_RESUBMIT % customer.last_name,
        customer.email
    )

@shared_task
def send_mail_resubmit(customer):
        send_mail(
        EMAIL_SUBJECT_SUBMIT,
        EMAIL_SUBMIT % customer.last_name,
        customer.email
    )


@shared_task
def check_request(customer):
    s3 = S3()
    imagga_ = Imagga_Request() 
    img1 = s3.get_object(customer.img1.name.split('/')[-1])
    img2 = s3.get_object(customer.img2.name.split('/')[-1])
    (dt1, face_id1) = imagga_.detect(img1)
    if (dt1 < 80.0):
        customer.state = "R"
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (customer.last_name,NO_FACE_IMG1),
        customer.email
        )
        return
    
    (dt2, face_id2) = imagga_.detect(img2)
    if (dt2 < 80.0):
        customer.state = "R"
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (customer.last_name,NO_FACE_IMG2),
        customer.email
        )
        return
    
    score = imagga_.similarity(face_id1, face_id2)
    if (score >= 80.0):
        customer.state = "A"
        send_mail(
            EMAIL_SUBJECT_APPROVED,
            EMAIL_SUBMIT % customer.last_name,
            customer.email
        )
        
    else:
        customer.state = "R"
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (customer.last_name, LOW_SIMILARITY),
        customer.email
        )