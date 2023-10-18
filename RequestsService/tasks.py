from celery import shared_task
from RequestsService.models import Customer
from RequestsService.S3Service import S3
from RequestsService.imagga import Imagga_Request
from RequestsService.Messages import *
from RequestsService.mailgun import send_mail


@shared_task
def send_mail_submit(ln, em):
    res = send_mail(
        EMAIL_SUBJECT_SUBMIT,
        EMAIL_SUBMIT % ln,
        em
    )
    # print(res.json())
    # return res.json()

@shared_task
def send_mail_resubmit(ln, em):
    res = send_mail(
        EMAIL_SUBJECT_RESUBMIT,
        EMAIL_RESUBMIT % ln,
        em
    )
    # return res.json()


@shared_task
def check_request(email, last_name, img1_path, img2_path):
    s3 = S3()
    imagga_ = Imagga_Request() 
    print(img1_path, img2_path)
    file1 = open('./staticfiles/web/media/%s' % img1_path, 'rb')
    file2 = open('./staticfiles/web/media/%s' % img2_path, 'rb')
    # img1 = s3.get_object(img1_path)
    # img2 = s3.get_object(img1_path)
    (dt1, face_id1) = imagga_.detect(file1)
    if (dt1 < 80.0):
        # customer.state = "R"
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (last_name,NO_FACE_IMG1),
        email
        )
        return
    
    (dt2, face_id2) = imagga_.detect(file2)
    if (dt2 < 80.0):
        # customer.state = "R"
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (last_name,NO_FACE_IMG2),
        email
        )
        return
    
    score = imagga_.similarity(face_id1, face_id2)
    if (score >= 80.0):
        # customer.state = "A"
        send_mail(
            EMAIL_SUBJECT_APPROVED,
            EMAIL_SUBMIT % last_name,
            email
        )
        
    else:
        # customer.state = "R"
        send_mail(EMAIL_SUBJECT_REJECT, 
        EMAIL_REJECTED % (last_name, LOW_SIMILARITY),
        email
        )