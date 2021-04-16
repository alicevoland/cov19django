from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from .views import TestView, RegionViewSet

router = routers.DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'test', TestView, 'toto')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('test', TestView.as_view())
]
