from django.db import models

# Create your models here.

class Region(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)