from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers
from . import models

# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer

#generics.ListAPIView: Handles only GET requests. Used when you want to return a list of items (like vendors) in JSON format. 
#queryset = models.Vendor.objects.all(): Tells DRF to fetch all records from the Vendor model.
#queryset : queryset is a special class attribute expected by Django REST Framework when you use generic views like ListAPIView, CreateAPIView

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorDetailSerializer

class ProductList(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductListSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer