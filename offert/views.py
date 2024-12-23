from django.shortcuts import render
from .serializers import OffertSerializers
from rest_framework import generics

from .models import Offert

# Create your views here.

class PostOffert(generics.ListCreateAPIView):
    serializer_class = OffertSerializers
    queryset = Offert.objects.all()
    