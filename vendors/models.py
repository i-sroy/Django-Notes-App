from django.db import models
from django.contrib.auth.models import AbstractUser

class MyVendor(AbstractUser):
    vendor_name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    REQUIRED_FIELDS = ['vendor_name']

# class MyUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     REQUIRED_FIELDS = ['email','password']




