# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# # Create your models here.

# class StaffSection(models.Model):

#     # id = models.AutoField("id", primary_key=True)
#     name = models.CharField("name", max_length=64)
#     members = models.ManyToManyField("boys.StaffMember", verbose_name="Member")
    
#     class Meta:
#         verbose_name ="StaffSection"
#         verbose_name_plural = "StaffSections"

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("StaffSection_detail", kwargs={"pk": self.pk})

# class StaffMember(models.Model):
    
#     # id = models.AutoField("id", primary_key=True)
#     full_name = models.CharField("full_name", max_length=50)
#     role = models.CharField("role",default='defrole', max_length=50)
#     img = models.ImageField(verbose_name='staff_img', null=True, blank=True)
    
#     class Meta:
#         verbose_name = "StaffMember"
#         verbose_name_plural = "StaffMembers"

#     def __str__(self):
#         return self.full_name

#     def get_absolute_url(self):
#         return reverse("StaffMember_detail", kwargs={"pk": self.pk})
