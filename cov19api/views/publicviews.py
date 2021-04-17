from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from cov19api.serializers import *
from cov19api.models import *


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all().order_by('code')
    serializer_class = RegionSerializer


class TestPublicView(ViewSet):
    def list(self, request):
        return Response({
            'view': 'TestPublicView',
            'authenticated': request.user.is_authenticated
        })
