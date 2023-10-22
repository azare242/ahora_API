from celery import shared_task
from RequestsService.models import Customer
from RequestsService.S3Service import S3
from RequestsService.imagga import Imagga_Request
from RequestsService.Messages import *
from RequestsService.mailgun import send_mail, validate_mail


@shared_task
def send_mail_submit(ln, em):
    validate_mail(em)
    send_mail(
        EMAIL_SUBJECT_SUBMIT,
        EMAIL_SUBMIT % ln,
        em
    )


@shared_task
def send_mail_resubmit(ln, em):
    res = send_mail(
        EMAIL_SUBJECT_RESUBMIT,
        EMAIL_RESUBMIT % ln,
        em
    )


@shared_task
def check_request(email, last_name, img1_path, img2_path):
    s3 = S3()
    imagga_ = Imagga_Request() 
    _c = Customer.objects.filter(email=email)[0]
    
    img1 = s3.get_object(img1_path)
    img2 = s3.get_object(img2_path)
    

    (dt1, face_id1) = imagga_.detect(img1)
    if (dt1 < 80.0):
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (last_name,NO_FACE_IMG1),
        email
        )
        print("%s REJECTED" % email)
        _c.state = "R"
        _c.save()
        
        return
    
    (dt2, face_id2) = imagga_.detect(img2)
    if (dt2 < 80.0):
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (last_name,NO_FACE_IMG2),
        email
        )
        print("%s REJECTED" % email)
        _c.state = "R"
        _c.save()
        return
    
    score = imagga_.similarity(face_id1, face_id2)
    if (score >= 80.0):
        send_mail(
            EMAIL_SUBJECT_APPROVED,
            EMAIL_APPROVED % last_name,
            email
        )
        print("%s APPROVED" % email)
        _c.state = "A"
        _c.save()
        
        
    else:
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (last_name, LOW_SIMILARITY),
        email
        )
        print("%s REJECTED" % email)
        _c.state = "R"
        _c.save()
        
        