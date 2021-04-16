from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import *
from .models import *


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('code')
    serializer_class = RegionSerializer