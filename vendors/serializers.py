from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyVendor
        fields = ['vendor_name','address','contact_details']