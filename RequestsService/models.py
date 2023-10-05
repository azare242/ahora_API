# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from hashid_field import HashidAutoField

states = [
    ("A", "Approved"),
    ("P", "Pending"),
    ("R", "Rejected")
]

class Customer(models.Model):
    
    email = models.EmailField(_("email"), max_length=254, null=False, unique=True)
    last_name = models.CharField(_("last name"), max_length=64, null=False)
    national_id = HashidAutoField(_("National ID"), null=False, unique=True,primary_key=True)
    user_ip = models.GenericIPAddressField(_("IP"), null=False, unique=False)
    # image1 = models.ImageField(_("IMG1"), upload_to='IMAGE1/')
    # image2 = models.ImageField(_("IMG2"), upload_to='IMAGE2/')
    state = models.CharField(_("State"), choices=states, null=False, max_length=20)