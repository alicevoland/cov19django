# Create your models here.
from django.db import models
from rest_framework.authentication import TokenAuthentication


class BearerAuthentication(TokenAuthentication):
    '''
    Simple token based authentication using utvsapitoken.

    Clients should authenticate by passing the token key in the 'Authorization'
    HTTP header, prepended with the string 'Bearer '.  For example:

    Authorization: Bearer 956e252a-513c-48c5-92dd-bfddc364e812
    '''
    keyword = 'Bearer'


class Region(models.Model):
    regionCode = models.CharField(max_length=10, unique=True)
    regionName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.regionCode} - {self.regionName}'


class Department(models.Model):
    departmentCode = models.CharField(max_length=10, unique=True)
    departmentName = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.departmentCode} - {self.departmentName}'
