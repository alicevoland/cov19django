from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from cov19api.models import BearerAuthentication


# See: https://gist.github.com/jsmedmar/d846eee063fa23148f8a87313dd590a3
class AuthRequiredMixin(AccessMixin):
    authentication_classes = [BearerAuthentication]

    def dispatch(self, request, *args, **kwargs):
        """Check Authorisation Bearer"""
        user = BearerAuthentication().authenticate(request)
        if user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return JsonResponse(
                data={'message': 'Unauthorized access'},
                status=HTTPStatus.UNAUTHORIZED
            )


class TestAuthView(AuthRequiredMixin, ViewSet):

    def list(self, request):
        return Response({
            'view': 'TestAuthView',
            'authenticated': request.user.is_authenticated
        })
