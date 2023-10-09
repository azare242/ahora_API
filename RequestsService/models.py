# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from hashid_field import HashidAutoField

states = [
    ("A", "Approved"),
    ("P", "Pending"),
    ("R", "Rejected")
]

def image_upload_path_img1(instance, filename):
    # Define the upload path for img1 based on the email field
    return f'images/img1/{instance.email}_img1.png'

def image_upload_path_img2(instance, filename):
    # Define the upload path for img2 based on the email field
    return f'images/img2/{instance.email}_img2.png'


class Customer(models.Model):
    
    email = models.EmailField(_("email"), max_length=254, null=False, unique=True)
    last_name = models.CharField(_("last name"), max_length=64, null=False)
    national_id = HashidAutoField(_("National ID"), null=False, unique=True,primary_key=True)
    user_ip = models.GenericIPAddressField(_("IP"), null=False, unique=False)
    state = models.CharField(_("State"), choices=states, null=False, max_length=20)
    img1 = models.ImageField(_("IMG1"), upload_to=image_upload_path_img1, null=True, blank=True)
    img2 = models.ImageField(_("IMG2"), upload_to=image_upload_path_img2, null=True, blank=True)
    # img1_confidence = models.FloatField(_("img1_confidence"), null=True, name="img1_confidence")
    # img2_confidence = models.FloatField(_("img2_confidence"), null=True, name="img2_confidence")
    # img1_faceid = models.CharField(_("img1_faceid"), max_length=1024)
    # img2_faceid = models.CharField(_("img2_faceid"), max_length=1024)
    