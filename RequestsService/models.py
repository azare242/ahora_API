from django.db import models
from django.utils.translation import gettext_lazy as _
from hashid_field import HashidAutoField

states = [
    ("A", "Approved"),
    ("P", "Pending"),
    ("R", "Rejected")
]

def image_upload_path_img1(instance, filename):
    return f'images/img1/{instance.email}_img1.png'

def image_upload_path_img2(instance, filename):
    return f'images/img2/{instance.email}_img2.png'


class Customer(models.Model):
    
    email = models.EmailField(_("email"), max_length=254, null=False, unique=True)
    last_name = models.CharField(_("last name"), max_length=64, null=False)
    national_id = HashidAutoField(_("National ID"), null=False, unique=True,primary_key=True)
    user_ip = models.GenericIPAddressField(_("IP"), null=False, unique=False)
    state = models.CharField(_("State"), choices=states, null=False, max_length=20)
    img1 = models.ImageField(_("IMG1"), upload_to=image_upload_path_img1, null=True, blank=True)
    img2 = models.ImageField(_("IMG2"), upload_to=image_upload_path_img2, null=True, blank=True)
    