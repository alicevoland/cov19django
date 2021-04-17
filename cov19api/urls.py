from django.urls import include, path
from rest_framework import routers

from cov19api.views.authviews import TestAuthView
from cov19api.views.publicviews import AuthToken, TestPublicView, RegionViewSet

router = routers.DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'test', TestPublicView, 'test')
router.register(r'auth/test', TestAuthView, 'test')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', AuthToken.as_view()),
]
