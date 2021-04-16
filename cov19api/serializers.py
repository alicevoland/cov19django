from rest_framework import serializers

from .models import *


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('code', 'name')
