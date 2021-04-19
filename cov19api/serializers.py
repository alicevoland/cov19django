from rest_framework import serializers

from cov19api import models


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Region
        fields = ('regionCode', 'regionName')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Department
        fields = ('departmentCode', 'departmentName', 'region')
