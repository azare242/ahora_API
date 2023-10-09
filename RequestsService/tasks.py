from celery import shared_task
from RequestsService.models import Customer
from RequestsService.S3Service import S3
from RequestsService.imagga import Imagga_Request




@shared_task
def check_request(customer):
    s3 = S3()
    imagga_ = Imagga_Request() 
    img1 = s3.get_object(customer.img1.name.split('/')[-1])
    img2 = s3.get_object(customer.img2.name.split('/')[-1])
    (dt1, face_id1) = imagga_.detect(img1)
    if (dt1 < 80.0):
        customer.state = "R"
        return
    
    (dt2, face_id2) = imagga_.detect(img2)
    if (dt2 < 80.0):
        customer.state = "R"
        return
    
    score = imagga_.similarity(face_id1, face_id2)
    if (score >= 80.0):
        customer.state = "A"
        
    else:
        customer.state = "R"