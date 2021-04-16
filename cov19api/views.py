from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from .serializers import *
from .models import *


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all().order_by('code')
    serializer_class = RegionSerializer


class TestView(ViewSet):
    def list(self, request):
        return Response({'test': 'test'})
