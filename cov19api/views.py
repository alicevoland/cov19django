# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from cov19api import models
from cov19api import serializers
from cov19api import services


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
    queryset = models.Region.objects.all().order_by('regionCode')
    serializer_class = serializers.RegionSerializer

class DepartmentViewSet(ModelViewSet):
    queryset = models.Department.objects.all().order_by('departmentCode')
    serializer_class = serializers.DepartmentSerializer



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

class TestUpdateViewSet(ViewSet):

    @action(detail=False, methods=['get'], name='Test Update')
    def go(self, request):
        services.fetch_departments_and_regions()
        return Response(
            data={
                'view': 'TestView titi',
            }
        )

