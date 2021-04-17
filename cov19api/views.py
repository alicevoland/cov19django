from django.http import JsonResponse
# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from cov19api.serializers import *


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
    """DOc"""

    def list(self, request):
        """DDD"""
        return Response({
            'view': 'TestPublicView',
            'authenticated': request.user.is_authenticated
        })


class TestAuthView(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        '''Doc'''
        return Response(
            data={
                'view': 'TestAuthView',
                'authenticated': request.user.is_authenticated
            }
        )
