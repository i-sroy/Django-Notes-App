from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from django import db
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout

class BasicAPI(generics.ListCreateAPIView):
    serializer_class = VendorSerializer
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        vendor = MyVendor.objects.create(vendor_name = serializer.data['vendor_name'], contact_details = serializer.data['contact_details'], address = serializer.data['address'])
        token,_ = Token.objects.get_or_create(key=vendor)
        print(token)
        print(serializer.data)
        return  Response({
            'token': str(token),
            'payload' : serializer.data
        })
    
    def get(self, request):
        permission_classes = [IsAuthenticated]
        vendor = MyVendor.objects.all()
        serializer = self.get_serializer(vendor, many=True)
        return Response(serializer.data)
        
class SpecificAPI(generics.RetrieveAPIView):
    serializer_class = VendorSerializer
    def get(self,request,pk):
        vendor = MyVendor.objects.filter(id = pk)
        serializer = self.get_serializer(vendor, many=True)
        return Response(serializer.data)
    
    def put(self,request,pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        vendor = MyVendor.objects.filter(id=pk).update(vendor_name = serializer.data['vendor_name'], contact_details = serializer.data['contact_details'], address = serializer.data['address'])
        return Response("Updated")
    
    def delete(self,request,pk):
        vendor = MyVendor.objects.filter(id = pk).delete()
        return Response("Deleted")




    

    

        

        



